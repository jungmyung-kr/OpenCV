"""
10. 이미지 변형 (흑백)
"""

#######################################################

#################
# 이미지를 흑백으로 읽음
#################

import cv2

img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

######################
# 불러온 이미지를 흑백으로 변경
######################
import cv2

img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

dst = cv2.cvtColor(img, cv2_COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.imshow('gray', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)