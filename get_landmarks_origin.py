# 원본 영상의 csv 파일 저장
import download_shorts, PoseDetection

video_url_add = input('원본 유튜브 링크 :')
download_results = download_shorts.download_video(video_url_add)
video_route = download_results['video_route']

lm_result = PoseDetection.get_landmarks(video_route)



# test link : https://www.youtube.com/shorts/5rHxqoJZG60