import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

import numpy as np
import pandas as pd

clm_list = [
    'l_shld_x','l_shld_y','l_shld_z','l_shld_vis',
    'r_shld_x','r_shld_y','r_shld_z','r_shld_vis',
    'l_elbw_x','l_elbw_y','l_elbw_z','l_elbw_vis',
    'r_elbw_x','r_elbw_y','r_elbw_z','r_elbw_vis',
    'l_wrst_x','l_wrst_y','l_wrst_z','l_wrst_vis',
    'r_wrst_x','r_wrst_y','r_wrst_z','r_wrst_vis',
    'l_hip_x','l_hip_y','l_hip_z','l_hip_vis',
    'r_hip_x','r_hip_y','r_hip_z','r_hip_vis',
    'l_knee_x','l_knee_y','l_knee_z','l_knee_vis',    
    'r_knee_x','r_knee_y','r_knee_z','r_knee_vis',
    'l_ankl_x','l_ankl_y','l_ankl_z','l_ankl_vis',
    'r_ankl_x','r_ankl_y','r_ankl_z','r_ankl_vis',
]

def get_landmarks(video_route):
    cap = cv2.VideoCapture(video_route)
    mp_pose = mp.solutions.pose
    mp_draw = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    pose = mp_pose.Pose()

    df = pd.DataFrame()        # 빈 dataframe 생성
    clm = pd.DataFrame(clm_list).T

    df = pd.concat([df, clm])
    print(df)


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
                    print(id, lm)

            cv2.imshow("Estimation", img)

            # 빈 리스트 x 생성
            x = []      

            for k in range(33):
                if (11 <= k < 17) | (23 <= k <29):
                    x.append(results.pose_landmarks.landmark[k].x)
                    x.append(results.pose_landmarks.landmark[k].y)
                    x.append(results.pose_landmarks.landmark[k].z)
                    x.append(results.pose_landmarks.landmark[k].visibility)

            # list x를 dataframe으로 변경
            tmp = pd.DataFrame(x).T

            # dataframe에 정보 쌓기(33개 landmarks의 (33*4, x y z, vis)132개 정보)
            df = pd.concat([df, tmp])

            df.to_csv("test.csv", index=False, header=False)
            cv2.waitKey(1)




