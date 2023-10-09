import librosa
import numpy as np
import moviepy.editor as mp

def MatchSync(vpath_1, vpath_2):
    # 비디오 파일 로드
    video1 = mp.VideoFileClip(vpath_1)
    video2 = mp.VideoFileClip(vpath_2)

    # Audio 파일 경로 설정
    mp3_file1 = "./data/audios/audio_1.mp3"
    mp3_file2 = "./data/audios/audio_2.mp3"

    # Audio 파일 생성
    print('Creating Audio files...')
    audio1 = video1.audio.write_audiofile(mp3_file1)
    audio2 = video2.audio.write_audiofile(mp3_file2)

    # Audio 파일 load
    print('Loading audio files...')
    y1, sr1 = librosa.load(mp3_file1)
    y2, sr2 = librosa.load(mp3_file2)

    # cross-correlation 계산
    print('Calculating Cross-Correlation...')
    correlation = np.correlate(y1, y2, mode='full')
    peak_index = np.argmax(correlation)         # peak index (correlation이 가장 큰 지점의 인덱스)
    print("peak index: ", peak_index)

    # sync 차이 계산 (peak 위치를 초 단위로 변환)
    sync_difference_seconds = (peak_index - len(y2) + 1) / sr1
    print(f"Sync difference: 약 {sync_difference_seconds:.2f}sec")
    return sync_difference_seconds