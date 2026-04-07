# Youtuber GPT

This project is designed to download a list of videos from a YouTube influencer, fetch transcript data for those videos, and build a searchable transcript database that can be used to ask questions about the influencer's speeches.

## What it does

- Extracts video metadata from a YouTube channel or playlist
- Fetches transcripts for each video using YouTube transcript services
- Saves transcript files locally for later processing
- Enables building a searchable database from the collected transcripts
- Supports question-answering over the influencer's spoken content

## Key files

- `video_list.py` - fetches video IDs and metadata, downloads transcripts, and stores them in JSONL format

## Libraries used

- `yt_dlp` - used to extract video lists and metadata from YouTube
- `youtube_transcript_api` - used to fetch video transcripts in Portuguese and supported languages

## Usage

1. Update the target YouTube channel URL in the script.
2. Run the script to download video metadata and transcripts.
3. Process the downloaded transcript files to build the question-answering database.

## Notes

This project is meant for building a dataset focused on a specific influencer's video transcripts and enabling downstream analysis or natural language querying of their speech content.
