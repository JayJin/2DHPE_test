import csv
import numpy as np
import math

from sklearn import preprocessing
from sklearn.metrics.pairwise import cosine_similarity
from match_audiosync import MatchSync

def Compare(lpath_1, lpath_2, sync_difference_seconds):
    diff = sync_difference_seconds
    # load data
    with open(lpath_1, 'r') as f:
        data1 = list(csv.reader(f, delimiter=","))
    with open(lpath_2, 'r') as f:
        data2 = list(csv.reader(f, delimiter=","))

    if diff > 0:
        ldmk_1 = np.array(data1)[1+diff:, 1:]
        ldmk_2 = np.array(data2)[1:, 1:]
    elif diff == 0:
        ldmk_1 = np.array(data1)[1:, 1:]
        ldmk_2 = np.array(data2)[1:, 1:]
    else:
        ldmk_1 = np.array(data1)[1:, 1:]
        ldmk_2 = np.array(data2)[1+(diff*(-1)+1):, 1:]

    r1, c1 = ldmk_1.shape   
    r2, c2 = ldmk_2.shape
    print('r1, c1, r2, c2:', r1, c1, r2, c2)

    length_val = min(r1, r2)
    print(f"length of landmarks: {length_val}")
    ldmk_1 = ldmk_1[:length_val]
    ldmk_2 = ldmk_2[:length_val]

    # normalize
    ldmk_1_normalized_l2 = preprocessing.normalize(ldmk_1, norm = 'l2')
    ldmk_2_normalized_l2 = preprocessing.normalize(ldmk_2, norm = 'l2')

    # Cosine Similarity
    cosine_sim = cosine_similarity(ldmk_1_normalized_l2, ldmk_2_normalized_l2)
    results = np.diag(cosine_sim)
    print("-----Results of Cosine Similarity-----")
    print(results)
    mean_score = np.mean(results)
    print(f"score: {str(round(mean_score*100, 1))}점")
    return results, mean_score



lpath_1 = "D:\JAY\\2DHPE_test\\2dhpe_test\data\landmarks\origin\\202310091739_스모크챌린지.csv"
lpath_2 = "D:\JAY\\2DHPE_test\\2dhpe_test\data\landmarks\\new\\202310091739_스모크챌린지 Choreo by 바다.csv"
# lpath_2 = "D:\JAY\\2DHPE_test\\2dhpe_test\data\landmarks\origin\\202310091739_스모크챌린지.csv"

vpath_1 = ".\data\\videos\\202310091700_스모크챌린지.mp4"
vpath_2 = ".\data\\videos\\202310091701_스모크챌린지 Choreo by 바다.mp4"
# vpath_2 = ".\data\\videos\\202310091700_스모크챌린지.mp4"

sync = MatchSync(vpath_1, vpath_2)
# print(math.ceil(sync * 10))
Compare(lpath_1, lpath_2, math.ceil(sync * 10))

