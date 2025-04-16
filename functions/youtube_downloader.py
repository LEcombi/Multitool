from yt_dlp import YoutubeDL
import os
def download_youtube_video(url, output_path="yt_downloads"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'outtmpl': f"{output_path}/%(title)s.%(ext)s",
        'format': 'best'
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
