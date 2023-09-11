from pytube import YouTube

DOWNLOAD_DIR = r"D:\WORK\\prj_3dhpe\data\\videos"

def download_video(video_url):
    yt = YouTube(video_url)
    yt.streams.filter(res='360p', file_extension='mp4').first().download(output_path=DOWNLOAD_DIR, filename = f'{yt.title}.mp4')

if __name__ == '__main__':
    video_url = 'https://www.youtube.com/shorts/ekgPbl78Cig'
    download_video(video_url)