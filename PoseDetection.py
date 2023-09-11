import cv2
import mediapipe as mp
import numpy as np

# Video 1
cap1 = cv2.VideoCapture('D:\WORK\prj_3dhpe\data\\videos\smoke_ch_02.mp4')

mp_pose1 = mp.solutions.pose
mp_draw1 = mp.solutions.drawing_utils
pose1 = mp_pose1.Pose()

# Video 2
cap2 = cv2.VideoCapture('D:\WORK\prj_3dhpe\data\\videos\smoke_ch_03.mp4')

mp_pose2 = mp.solutions.pose
mp_draw2 = mp.solutions.drawing_utils
pose2 = mp_pose2.Pose()

while True:
    # Video 1
    ret1, img1 = cap1.read()
    img1 = cv2.resize(img1, (200, 400))
    results1 = pose1.process(img1)

    # 랜드마크 생성(1)
    mp_draw1.draw_landmarks(img1, results1.pose_landmarks, mp_pose1.POSE_CONNECTIONS,
                           mp_draw1.DrawingSpec((255, 0, 0), 2, 2),      # DrawingSpec : landmark 색상, 두께, 반경 지정
                           mp_draw1.DrawingSpec((255, 0, 255), 2, 2))      # DrawingSpec : connection line 색상, 두께, 반경 지정
    cv2.imshow("Estimation_01", img1)
    h1, w1, c1 = img1.shape


    # Video 2
    ret2, img2 = cap2.read()
    img2 = cv2.resize(img2, (200, 400))
    results2 = pose2.process(img2)

    # 랜드마크 생성(2)
    mp_draw2.draw_landmarks(img2, results2.pose_landmarks, mp_pose2.POSE_CONNECTIONS,
                           mp_draw2.DrawingSpec((255, 0, 0), 2, 2),      # DrawingSpec : landmark 색상, 두께, 반경 지정
                           mp_draw2.DrawingSpec((255, 0, 255), 2, 2))      # DrawingSpec : connection line 색상, 두께, 반경 지정
    cv2.imshow("Estimation_02", img2)
    h2, w2, c2 = img2.shape


    # 비교 이미지 생성
    # opImg = np.zeros([h1, w1, c1])

    # # opImg.fill(0)     # 배경을 특정색상으로 지정
    # mp_draw.draw_landmarks(opImg, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
    #                        mp_draw.DrawingSpec((255, 0, 0), 2, 2),      # DrawingSpec : landmark 색상, 두께, 반경 지정
    #                        mp_draw.DrawingSpec((255, 0, 255), 2, 2))      # DrawingSpec : connection line 색상, 두께, 반경 지정
    # cv2.imshow("Extracted Pose", opImg)    

    # print(results.pose_landmarks)

    cv2.waitKey(1)