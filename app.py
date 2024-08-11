from pytubefix import YouTube
from pytubefix.cli import on_progress
import os


def download_youtube_video(url, dl_path, resolution="1080p"):
    try:
        yt = YouTube(
            url,
            on_progress_callback=on_progress,
        )

        # filter for video stream with the desired resolution
        video_stream = yt.streams.filter(
            adaptive=True,
            file_extension="mp4",
            res=resolution).first()
        # filter for audio stream
        audio_stream = yt.streams.filter(
            only_audio=True,
            file_extension="mp4").first()

        if not video_stream:
            print(f"No video found for the resolution {resolution}.")
            return
        if not audio_stream:
            print("No audio stream found.")
            return

        # download the video stream
        print("Downloading video...")
        video_stream.download(output_path=dl_path)
        print("Video downloaded successfully.")

        # Download the audio stream
        print("Downloading audio...")
        audio_stream.download(mp3=True, output_path=dl_path)
        print("Audio downloaded successfully.")
        print(f"Files saved at {dl_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    dl_path = os.path.expanduser("~/Downloads")
    url = input("Enter YouTube video URL: ").strip()

    if not url:
        print("Invalid URL. Please enter a valid YouTube URL.")
    else:
        download_youtube_video(url, dl_path)
