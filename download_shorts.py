from pytube import YouTube
from datetime import datetime

now = datetime.now()

DOWNLOAD_DIR = r"./data/videos"

def download_video(video_url):
    yt = YouTube(video_url)
    video_title = (str(now.strftime('%Y%m%d%H%M'))+"_"+yt.title.split('#')[1]).rstrip()
    yt.streams.filter(res='360p', file_extension='mp4').first().download(output_path=DOWNLOAD_DIR, filename = f'{video_title}.mp4')
    video_route = f'./data/videos/{video_title}.mp4'
    print(video_route)
    return video_route

# 직접 실행시
# if __name__ == '__main__':
#     video_url = 'https://www.youtube.com/shorts/ekgPbl78Cig'
#     download_video(video_url)