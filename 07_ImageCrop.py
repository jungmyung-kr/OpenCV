"""
07. 이미지 자르기
"""

#######################################################

# 영역을 잘라서 새로운 윈도우(창)에 표시

import cv2
img = cv2.imread('img.jpg')
img.shape # (433, 640, 3)

crop = img[200:350, 200:400]
# 세로범위, 가로범위

cv2.imshow('img', img) # 원본이미지
cv2.imshow('crop', crop) # 잘린 이미지
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

# 영역을 잘라서 기존 윈도우에 표시

import cv2
img = cv2.imread('img.jpg')
img.shape # (433, 640, 3)

crop = img[200:350, 200:400]
# 세로범위, 가로범위

img[200:350, 400:600] = crop  # 원래 이미지 옆에 나열하기 위해 좌표값을 다르게 설정

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)