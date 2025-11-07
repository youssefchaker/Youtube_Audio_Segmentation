# YouTube Audio Downloader

This Python script allows you to download audio from YouTube videos, either the full audio or specific segments.

## Features

*   Download full audio from a YouTube video.
*   Download specific audio segments from a YouTube video.
*   Command-line interface for easy interaction.

## Requirements

*   Python 3.6+
*   FFmpeg

## Installation

1.  Clone this repository or download the files.
2.  Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```
3.  Download the latest FFmpeg essentials build from [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/).
4.  Extract the downloaded file and place the `ffmpeg-*-essentials_build` folder into the root of the project directory. The script is configured to locate ffmpeg within this folder.

## Usage

Run the script from your terminal:

```
python main.py
```

The script will present you with a menu of options:

1.  **Download full video audio**: Prompts for a YouTube video URL and downloads the entire audio track.
2.  **Download video audio segment**: Prompts for a YouTube video URL, a start time (HH:MM:SS), and an end time (HH:MM:SS) to download a specific audio segment.
3.  **Exit**: Exits the application.

The downloaded audio files will be saved in the `output` directory, with filenames formatted as `<video_title>_<start_time>_<end_time>.mp3` for segments, and `<video_title>.mp3` for full audio.