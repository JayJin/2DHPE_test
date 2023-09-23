import download_shorts, PoseDetection
import os, glob


video_url_add = input('신규 유튜브 링크 :')
download_results = download_shorts.download_video(video_url_add)

chl_name = download_results['challenge_name']
lm_path = '/data/landmarks/'

end_str = f'{chl_name}.mp4'
for f in glob.glob(f'data/landmarks/*{end_str}.csv'):
    print("확인")
    print(f)

print('1')
print(chl_name)
print('2')
print(lm_path)


video_route = download_results['video_route']

lm_result = PoseDetection.get_landmarks(video_route)


# Compare

# test link : https://www.youtube.com/shorts/5rHxqoJZG60