"""
12. 이미지 변형 (원근)
"""

#######################################################

#####################
# 사다리꼴 이미지 펼치기
#####################

import cv2
import numpy as np

img = cv2.imread('newspaper.jpg')

width, height = 640, 240
src = np.array([[511, 352], [1008, 345], [1122, 584], [455, 594]], dtype=np.float32)  # input 4개 지정
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)
# 좌상, 우상, 우하, 좌하 (시계 방향으로 4지점 정의)

matrix = cv2.getPerspectiveTransform(src, dst)  # src를 dst로 변환하기 위한 matrix 얻어옴
result = cv2.warpPerspective(img, matrix, (width, height))  # matrix대로 변환 함

cv2.imshow('img', img)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

#####################
# 회전된 이미지 올바로 세우기
#####################

import cv2
import numpy as np

img = cv2.imread('poker.jpg')

width, height = 530, 710
src = np.array([[702, 143], [1133, 414], [726, 1007], [276, 700]], dtype=np.float32)  # input 4개 지정
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)
# 좌상, 우상, 우하, 좌하 (시계 방향으로 4지점 정의)

matrix = cv2.getPerspectiveTransform(src, dst)  # src를 dst로 변환하기 위한 matrix 얻어옴
result = cv2.warpPerspective(img, matrix, (width, height))  # matrix대로 변환 함

cv2.imshow('img', img)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

#######################################################

#####################
# 마우스 이벤트 등록
#####################

import cv2

def mouse_handler(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스 왼쪽 버튼 down
        print('왼쪽 버튼 Down')
        print(x, y)
    elif event == cv2.EVENT_LBUTTONUP:  # 마우스 왼쪽 버튼 up
        print('왼쪽 버튼 UP')
        print(x, y)
    elif event == cv2.EVENT_LBUTTONDBLCLK:  # 마우스 왼쪽 버튼 더블 클릭
        print('왼쪽 버튼 Double Click')
    # elif event == cv2.EVENT_MOUSEMOVE:
    #    print('마우스 이동')
    elif event == cv2.EVENT_RBUTTONDOWN:  # 마우스 오른쪽 버튼 down
        print('오른쪽 버튼 Down')


img = cv2.imread('poker.jpg')
cv2.namedWindow('img')  # 이름을 줘서 윈도우를 먼저 만들어 두는 것, 여기에 마우스 이벤트를 처리하기 위한 핸들러 적용
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)