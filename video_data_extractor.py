import json
import yt_dlp
from yt_dlp.utils import DownloadError

VIDEO_URL = "https://www.youtube.com/@NicholasRenotte/shorts"

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

def get_all_videos_infos(url, playlist_items=1):
    videos_infos = get_video_info(url, playlist_items)
    video_data = {}
    for video_info in videos_infos:
        title = get_title(video_info)
        video_data[title] = {}
        video_data[title]["audio_url"] = get_audio_url(video_info)
        video_data[title]["video_url"] = get_video_url(video_info)
    return  video_data

def save_video_info_json(videos):
    filename = 'video_info.json'
    with open(filename, 'w', encoding='UTF-8') as file_object:
        json.dump(videos, file_object)
    file_object.close()

if __name__ == "__main__":
    all_videos_infos = get_all_videos_infos(VIDEO_URL, playlist_items=10)
    save_video_info_json(all_videos_infos)
