#!/usr/bin/env python3
import yt_dlp
import ffmpeg
import os
from tqdm import tqdm
import shutil

FFMPEG_PATH = os.path.join(os.path.dirname(__file__), 'ffmpeg-2025-11-06-git-222127418b-essentials_build', 'ffmpeg-2025-11-06-git-222127418b-essentials_build', 'bin')
os.environ["PATH"] += os.pathsep + FFMPEG_PATH

def download_audio_segment(youtube_url, start_time, end_time, output_filename):
    """
    Downloads a specific audio segment from a YouTube video.

    Args:
        youtube_url (str): The URL of the YouTube video.
        start_time (str): The start time of the audio segment in HH:MM:SS format.
        end_time (str): The end time of the audio segment in HH:MM:SS format.
        output_filename (str): The name of the output audio file.
    """
    
    # Create a temporary directory to store the downloaded audio
    if not os.path.exists("temp"):
        os.makedirs("temp")

    pbar = tqdm(total=100, unit='%', desc="Downloading")

    def progress_hook(d):
        if d['status'] == 'downloading':
            pbar.total = d['total_bytes']
            pbar.update(d['downloaded_bytes'] - pbar.n)
        if d['status'] == 'finished':
            pbar.n = pbar.total
            pbar.close()

    # Download the full audio of the video
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "temp/%(id)s.%(ext)s",
        "progress_hooks": [progress_hook],
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=True)
        audio_file = ydl.prepare_filename(info_dict).replace(info_dict['ext'], 'mp3')


    # Cut the audio to the specified time range
    (
        ffmpeg
        .input(audio_file, ss=start_time, to=end_time)
        .output(output_filename)
        .run()
    )

    # Clean up the temporary audio file
    os.remove(audio_file)

if __name__ == "__main__":
    while True:
        print("Choose an option:")
        print("1. Process a video")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            youtube_url = input("Enter the YouTube URL: ")
            start_time = input("Enter the start time (HH:MM:SS): ")
            end_time = input("Enter the end time (HH:MM:SS): ")
            output_dir = "output"
            
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            output_filename = os.path.join(output_dir, f"{youtube_url.split('v=')[1]}_{start_time.replace(':', '-')}_{end_time.replace(':', '-')}.mp3")

            try:
                print(f"Downloading audio segment from {youtube_url} between {start_time} and {end_time}...")
                download_audio_segment(youtube_url, start_time, end_time, output_filename)
                print(f"Successfully downloaded {output_filename}")
            except Exception as e:
                print(f"Error downloading {youtube_url}: {e}")

        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

    # Clean up the temporary directory
    if os.path.exists("temp"):
        shutil.rmtree("temp")