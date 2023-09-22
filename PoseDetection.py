import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

import numpy as np
import pandas as pd

labels = {'0' : 'nose',
'1' : 'left eye (inner)',
'2' : 'left eye',
'3' : 'left eye (outer)',
'4' : 'right eye (inner)',
'5' : 'right eye',
'6' : 'right eye (outer)',
'7' : 'left ear',
'8' : 'right ear',
'9' : 'mouth (left)',
'10' : 'mouth (right)',
'11' : 'left shoulder',         # ★
'12' : 'right shoulder',        # ★
'13' : 'left elbow',            # ★
'14' : 'right elbow',           # ★
'15' : 'left wrist',            # ★
'16' : 'right wrist',           # ★
'17' : 'left pinky',
'18' : 'right pinky',
'19' : 'left index',
'20' : 'right index',
'21' : 'left thumb',
'22' : 'right thumb',
'23' : 'left hip',              # ★
'24' : 'right hip',             # ★
'25' : 'left knee',             # ★    
'26' : 'right knee',            # ★
'27' : 'left ankle',            # ★
'28' : 'right ankle',           # ★
'29' : 'left heel',
'30' : 'right heel',
'31' : 'left foot index',
'32' : 'right foot index'}

# Video 1
cap = cv2.VideoCapture('D:\WORK\prj_3dhpe\data\\videos\smoke_ch_02.mp4')
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
pose = mp_pose.Pose()
df = pd.DataFrame()        # 빈 dataframe 생성

with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
    while True:
        ret, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (200, 400))
        results = pose.process(img)
        
        # 랜드마크 생성
        if results.pose_landmarks:
            mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)

        cv2.imshow("Estimation", img)

        # 빈 리스트 x 생성
        x = []      

        # 'left shoulder','right shoulder','left elbow','right elbow','left wrist','right wrist','left hip','right hip','left knee','right knee','left ankle','right ankle'
        # k - landmarks 개수
        # results.pose_landmarks.landmark[k].x/y/z/visibility로 k번째 landmarks의 정보를 가져올 수 있다
        # x.append()
        for k in range(33):
            # if (11 <= k < 17) | (23 <= k <29):
            x.append(results.pose_landmarks.landmark[k].x)
            x.append(results.pose_landmarks.landmark[k].y)
            x.append(results.pose_landmarks.landmark[k].z)
            x.append(results.pose_landmarks.landmark[k].visibility)
        # x.append(results.pose_landmarks.landmark[0].x)
        # x.append(results.pose_landmarks.landmark[0].y)
        # x.append(results.pose_landmarks.landmark[0].z)
        # x.append(results.pose_landmarks.landmark[0].visibility)

        # list x를 dataframe으로 변경
        tmp = pd.DataFrame(x).T

        # dataframe에 정보 쌓기(33개 landmarks의 (33*4, x y z, vis)132개 정보)
        df = pd.concat([df, tmp])

        df.to_csv("test.csv")
        cv2.waitKey(1)
        print(df)




