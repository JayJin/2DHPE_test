import download_shorts, PoseDetection
import os, glob


video_url_add = input('신규 유튜브 링크 :')
while True:
    try:
        n_o = input('new or origin (n/o):')
        if n_o == "n":
            file_type = 'new'
            break
        elif n_o == 'o':
            file_type = 'origin'
            break
    except:
        print("잘못된 입력값입니다. 다시 입력해주세요")

print(file_type)
download_results = download_shorts.download_video(video_url_add)

chl_name = download_results['challenge_name']
lm_path = f'/data/landmarks/{file_type}'

end_str = f'{chl_name}.mp4'
for f in glob.glob(f'data/landmarks/{file_type}/*{end_str}.csv'):
    print("확인")
    print(f)

print('1')
print(chl_name)     # 챌린지 이름
print('2')
print(lm_path)      # landmark 경로


video_route = download_results['video_route']

lm_result = PoseDetection.get_landmarks(video_route, file_type)


# Compare

# test link : https://www.youtube.com/shorts/5rHxqoJZG60
# test link2 : https://www.youtube.com/shorts/7Sakx1F8AIs