import csv
import numpy as np
import math

from sklearn import preprocessing
from sklearn.metrics.pairwise import cosine_similarity
from match_audiosync import MatchSync

def Compare(lpath_1, lpath_2, sync_difference_seconds):
    diff = sync_difference_seconds
    # load data
    if diff > 0:
        with open(lpath_1, 'r') as f:
            data = list(csv.reader(f, delimiter=","))
        ldmk_1 = np.array(data)[1+diff:, 1:]
        r1, c1 = ldmk_1.shape
        print('r1, c1:', r1, c1)

        with open(lpath_2, 'r') as f:
            data = list(csv.reader(f, delimiter=","))
        ldmk_2 = np.array(data)[1:, 1:]
        r2, c2 = ldmk_2.shape
        print('r2, c2:', r2, c2)
    else:
        with open(lpath_1, 'r') as f:
            data1 = list(csv.reader(f, delimiter=","))
        ldmk_1 = np.array(data1)[1:, 1:]
        r1, c1 = ldmk_1.shape
        print('r1, c1:', r1, c1)

        with open(lpath_2, 'r') as f:
            data2 = list(csv.reader(f, delimiter=","))
        ldmk_2 = np.array(data2)[1+(diff*(-1)+1):, 1:]
        r2, c2 = ldmk_2.shape
        print('r2, c2:', r2, c2)

    length_val = min(r1, r2)
    ldmk_1 = ldmk_1[:length_val]
    ldmk_2 = ldmk_2[:length_val]

    # normalize
    ldmk_1_normalized_l2 = preprocessing.normalize(ldmk_1, norm = 'l2')
    ldmk_2_normalized_l2 = preprocessing.normalize(ldmk_2, norm = 'l2')
    print(ldmk_1_normalized_l2)
    print(ldmk_2_normalized_l2)

    print("한 행씩 출력")
    print(ldmk_1_normalized_l2[0])
    print(ldmk_2_normalized_l2[0])

    print("코사인 유사도 계산")
    cosine_sim = cosine_similarity(ldmk_1_normalized_l2[0], ldmk_2_normalized_l2[0])
    print(cosine_sim.shape)
    print(cosine_sim)
    # # Cosine Similarity
    # for i in range(1, length_val):
    #     cosine_sim = cosine_similarity(ldmk_1_normalized_l2[i], ldmk_2_normalized_l2[i])
    #     print('코사인 유사도 연산 결과 :',cosine_sim)



lpath_1 = "D:\JAY\\2DHPE_test\\2dhpe_test\data\landmarks\origin\\202310091739_스모크챌린지.csv"
lpath_2 = "D:\JAY\\2DHPE_test\\2dhpe_test\data\landmarks\\new\\202310091739_스모크챌린지 Choreo by 바다.csv"

vpath_1 = ".\data\\videos\\202310091700_스모크챌린지.mp4"
vpath_2 = ".\data\\videos\\202310091701_스모크챌린지 Choreo by 바다.mp4"


# ★ TEST 확인 완료시 복구해야 함!!!!!!!   - Cross Cor 동작 시간으로 현재 주석처리함
# sync = MatchSync(vpath_1, vpath_2)
# print(math.ceil(sync * 10))
# Compare(lpath_1, lpath_2, math.ceil(sync * 10))

# TEST
Compare(lpath_1, lpath_2, -6)