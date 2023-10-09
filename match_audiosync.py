import librosa
import numpy as np
import moviepy.editor as mp

# 비디오 파일 로드
video1 = mp.VideoFileClip("./data/videos/202310091054_스모크챌린지 Choreo by 바다 l Smoke (Prod. Dynamicduo, Padi) - 다이나믹 듀오, 이영지.mp4")
video2 = mp.VideoFileClip("./data/videos/202310091054_스모크챌린지.mp4")


# 두 개의 MP3 파일 경로 설정
mp3_file1 = "./data/audios/test1.mp3"
mp3_file2 = "./data/audios/test1_3_5s.mp3"

# 오디오 파일 생성
audio1 = video1.audio.write_audiofile(mp3_file1)
audio2 = video2.audio.write_audiofile(mp3_file2)

# librosa를 사용하여 MP3 파일 읽기
print('파일 로드 중...')
y1, sr1 = librosa.load(mp3_file1)
y2, sr2 = librosa.load(mp3_file2)


# cross-correlation 계산
print('cross correlation 계산 중...')
correlation = np.correlate(y1, y2, mode='full')
peak_index = np.argmax(correlation)         # peak index (correlation이 가장 큰 지점의 인덱스)

# sync 차이 계산 (peak 위치를 초 단위로 변환)
sync_difference_seconds = (peak_index - len(y2) + 1) / sr1
print(f"두 MP3 파일의 sync 차이는 약 {sync_difference_seconds:.2f} 초입니다.")