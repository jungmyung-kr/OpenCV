"""
08. 이미지 대칭
"""

#######################################################

##############
# 좌우 대칭
##############

import cv2
img = cv2.imread('img.jpg')
flip_horizontal = cv2.flip(img, 1)  # flipCode > 0 : 좌우 대칭

cv2.imshow('img', img)
cv2.imshow('flip', flip_horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

##############
# 상하 대칭
##############

import cv2
img = cv2.imread('img.jpg')
flip_vertical = cv2.flip(img, 0)  # flipCode = 0 : 상하 대칭

cv2.imshow('img', img)
cv2.imshow('flip', flip_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

##############
# 상하좌우 대칭
##############

import cv2
img = cv2.imread('img.jpg')
flip_both = cv2.flip(img, -1)  # flipCode < 0 : 상하좌우 대칭

cv2.imshow('img', img)
cv2.imshow('flip', flip_both)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)