"""
09. 이미지 회전
"""

#######################################################

##############
# 시계 방향 90도 회전
##############

import cv2
img = cv2.imread('img.jpg')

rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('img', img)
cv2.imshow('rotate_90', rotate_90)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

##############
# 180도 회전
##############

import cv2
img = cv2.imread('img.jpg')

rotate_180 = cv2.rotate(img, cv2.ROTATE_180)

cv2.imshow('img', img)
cv2.imshow('rotate_180', rotate_180)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

##################################
# 시계 반대 방향 90도 회전 (시계 방향 270도 회전)
##################################

import cv2
img = cv2.imread('img.jpg')

rotate_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
# 시계 반대 방향으로 90도

cv2.imshow('img', img)
cv2.imshow('rotate_270', rotate_270)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)