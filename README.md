# Youtuber GPT

This project is designed to download a list of videos from a YouTube influencer, fetch transcript data for those videos, and build a searchable transcript database that can be used to ask questions about the influencer's speeches.

## What it does

- Extracts video metadata from a YouTube channel or playlist
- Fetches transcripts for each video using YouTube transcript services
- Saves transcript files locally for later processing
- Enables building a searchable database from the collected transcripts
- Supports question-answering over the influencer's spoken content

## Key files

- `src/video_list.py` - fetches video IDs and metadata, downloads transcripts, and stores them in JSONL format
- `src/youtuber_gpt.py` - the main script orchestrating the data preparation

## Libraries used

- `yt_dlp` - used to extract video lists and metadata from YouTube
- `youtube_transcript_api` - used to fetch video transcripts in Portuguese and supported languages

## Usage

### Environment:
- Install Git if not already installed.
- Clone the repository (`git clone https://github.com/paulopessoasilva/youtuber-gpt`)
- Install Python if not already installed (project was tested with Python 3.12.10)
- Create a virtual environment: `python -m venv venv`
- Activate virtual environment: (Windows Command Prompt): `venv\Scripts\Activate.bat`
- Install uv: `pip install uv`
- Install requirements: `uv pip install -r requirements.txt` 

### Script:
- Update the target YouTube channel URL in `src\youtuber_gpt.py`.
- Run the script to download video metadata and transcripts: (Windows) `python src\youtuber_gpt.py`
- Process the downloaded transcript files to build the question-answering database.

## Notes

This project is meant for building a dataset focused on a specific influencer's video transcripts and enabling downstream analysis or natural language querying of their speech content.
