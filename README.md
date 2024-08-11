# YouTube Video Downloader

This Python script allows you to download both video and audio from YouTube
videos. It uses the pytubefix library to fetch streams and download them
to your local machine.

## Features

- Downloads video in 720p resolution (or any specified resolution).
- Downloads the corresponding audio stream separately.
- Provides real-time download progress updates.
- Saves the video and audio files in the specified download directory (default: ~/Downloads).

## Requirements

Python 3.7 or later. The dependencies are listed in the requirements.txt file.

## How to use:
1. Clone the repository:

    ```
    git clone https://github.com/arfeloreed/ytVid-dl.git
    cd ytVid-dl
    ```

2. Create a virtual environment (optional but recommended):

    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required packages:

    ```pip install -r requirements.txt```

4. Run the script:

    ```python downloader.py```

5. Input the YouTube URL when prompted:

    ```Enter YouTube video URL: <Your YouTube URL here>```

The downloaded files will be saved in your ~/Downloads folder by default.

### Example

```
$ python downloader.py
Enter YouTube video URL: https://www.youtube.com/watch?v=NL8D8EkphUw
Downloading video...
Video downloaded successfully.
Downloading audio...
Audio downloaded successfully.
Files saved at /home/username/Downloads
```

## Error Handling

If the script encounters an issue, it will output an error message specifying
the problem, whether it's a network issue, an invalid URL, or another issue.

## Troubleshooting

- **No video found for filter parameters:** This means that the video stream
        in the specified resolution (e.g., 720p) does not exist. Try changing the
        resolution in the script.
- **No audio stream found:** The script was unable to find an audio-only
        stream. Ensure the video URL is correct and try again.
- **HTTP Error 400: Bad Request:** Double-check the provided URL or your internet connection.

**_Note:_** The script is configured to run in a Linux environment.
