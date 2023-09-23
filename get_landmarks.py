import download_shorts, PoseDetection

video_url = input('유튜브 링크를 입력하시오 :')

download_results = download_shorts.download_video(video_url)

video_route = download_results[0]
PoseDetection.get_landmarks(video_route)