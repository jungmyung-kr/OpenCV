"""
01. 이미지 출력
"""

import cv2

img = cv2.imread('img.jpg') # 해당 경로의 파일 읽어오기
cv2.imshow('img', img)
cv2.waitKey(0) # 지정된 시간 동안 사용자 키 입력 대기
cv2.destroyAllWindows() # 모든 창 닫기
cv2.waitKey(1)

# 읽기 옵션
'''
cv2.IMREAD_COLOR : 컬러 이미지. 투명 영역은 무시 (기본값)
cv2.IMREAD_GRAYSCALE : 흑백 이미지
cv2.IMREAD_UNCHANGED : 투명 영역까지 포함
'''

img_color = cv2.imread('img.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread('img.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('img', img_color)
cv2.imshow('img', img_gray)
cv2.imshow('img', img_unchanged)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
cv2.waitKey(1)

# shape
# 이미지의 height, width, channel 정보

img = cv2.imread('img.jpg')
img.shape # 세로, 가로, channel : (433, 640, 3)