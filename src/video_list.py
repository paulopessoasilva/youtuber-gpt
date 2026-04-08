import json
import os
import random
import shutil
import time

import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi


def get_channel_videos(channel_url):
    ydl_opts = {
        "extractor_args": {"youtube": {"lang": ["pt", "pt-pt", "en"]}},
        "no_warnings": True,
        "quiet": True,
        "verbose": False,
        "extract_flat": False,
        "force_generic_extractor": False,
        "ignoreerrors": True,
        "playlist_items": "1-5",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(channel_url, download=False)
        if "entries" in result:
            return [
                {
                    "id": entry["id"],
                    "title": entry["title"],
                    "url": entry["webpage_url"],
                    "date": entry.get("upload_date", "0"),
                    "duration": entry.get("duration", 0),
                }
                for entry in result["entries"]
                if entry
            ]
    return []


def save_video_list(video_list, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for video in video_list:
            f.write(f"{json.dumps(video, ensure_ascii=False)}\n")


def load_video_list(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return [json.loads(line) for line in f if line.strip()]


def get_or_update_video_list(filename, channel_url):
    if os.path.exists(filename):
        file_age = time.time() - os.path.getmtime(filename)
        if file_age < 7 * 24 * 3600:  # 7 days in seconds
            print(f"Using cached video list from {filename} (age: {file_age/3600:.2f} hours)")
            return load_video_list(filename)

    print(f"Fetching new video list from channel: {channel_url}", end=" ")
    start_time = time.time()
    video_list = get_channel_videos(channel_url)
    elapsed_time = time.time() - start_time
    print(f"done ({elapsed_time:.2f}s)")
    save_video_list(video_list, filename)
    return video_list


def get_video_transcripts(video_list, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    ytt_api = YouTubeTranscriptApi()

    downloaded_any = False
    for i, video in enumerate(video_list):

        v_id = video["id"]
        filename = os.path.join(target_folder, f"{v_id}.jsonl")

        # Skips if already exists (automatic checkpoint)
        if os.path.exists(filename):
            print(f"[{i+1}/{len(video_list)}] Transcript for {v_id} already exists. Skipping...")
            continue

        try:
            print(f"[{i+1}/{len(video_list)}] Downloading: {v_id}...", end=" ")

            # Pause before each new download, except before the first actual download.
            if downloaded_any:
                wait_seconds = random.uniform(3, 7)
                print(f"waiting {wait_seconds:.2f}s...", end=" ")
                wait_start = time.time()
                time.sleep(wait_seconds)
                wait_elapsed = time.time() - wait_start
                print(f"waited {wait_elapsed:.2f}s... downloading...", end=" ")

            start_time = time.time()
            transcript = ytt_api.fetch(video_id=v_id, languages=["pt-BR", "pt"])

            with open(filename, "w", encoding="utf-8") as f:
                # The first line is the video metadata, and the rest are the transcript lines.
                f.write(f"{json.dumps(video, ensure_ascii=False)}\n")
                for line in transcript:
                    f.write(f"{json.dumps(line.__dict__, ensure_ascii=False)}\n")

            elapsed_time = time.time() - start_time
            print(f"done ({elapsed_time:.2f}s)")
            downloaded_any = True

        except Exception as e:
            print(f"Cannot download {v_id}. Reason: {e}")
            time.sleep(5)  # Pause before trying the next


def wipe_video_list_cache(filename):
    if os.path.exists(filename):
        os.remove(filename)

def wipe_folder(folder_path):
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
