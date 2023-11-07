import yt_dlp
from yt_dlp.utils import DownloadError
import json

def get_video_info(url, playlist_items=1):
    if playlist_items > 1:
        ydl_opts = {
        'playlist_items': '1-' + str(playlist_items),
    }
    else:
        ydl_opts = {
        'playlist_items': 1,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(
                url,
                download=False
            )
        except DownloadError:
            return None
        
    if 'entries' in result:
        list_videos = [video for video in result['entries']]
        video = list_videos
    else:
        video = result
    return video


def get_audio_url(video):
    for f in video['formats']:
        if f['ext'] == 'm4a':
            return f['url']

def get_title(video):
    return video['title']

def get_video_url(video):
    url_video = "https://www.youtube.com/watch?v=" + video['id']
    return url_video

if __name__ == '__main__':
    video_info = get_video_info("https://www.youtube.com/watch?v=giO92FBk33c")
    print(video_info)
    url = get_audio_url(video_info)
    print(url)
