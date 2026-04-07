import sys
import src.video_list as video_list

CHANNEL_URL = "https://www.youtube.com/@brunoreikdal_oficial/videos"
VIDEO_LIST_FILE = "data/video_list.jsonl"
TARGET_FOLDER = "data/transcripts"

video_list.wipe_video_list_cache(VIDEO_LIST_FILE)
video_list.wipe_folder(TARGET_FOLDER)
videos = video_list.get_or_update_video_list(filename=VIDEO_LIST_FILE, channel_url=CHANNEL_URL)
video_list.get_video_transcripts(videos, target_folder=TARGET_FOLDER)