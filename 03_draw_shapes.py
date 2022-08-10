import cv2
import numpy as np

'''
도형 그리기
'''

#######################################################

##############
# 빈 스케치북 만들기
##############

# 세로 480 * 가로 640, 3 channel (RGB)에 해당하는 스케치북 만들기
img = np.zeros((480, 640, 3), dtype=np.uint8)
# img[:] = (255, 255, 255) # 전체 공간을 흰 색으로 채우기 (참고 : B, G, R 순서)
# print(img)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

##############
# 일부 영역 색칠
##############

img = np.zeros((480, 640, 3), dtype=np.uint8) # (세로, 가로, 채널)
img[100:200, 200:300] = (255, 255, 255)
# [세로영역, 가로영역]

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

##############
# 직선
##############
'''
직선의 종류 (line type)

cv2.LINE_4 : 상하좌우 4방향으로 연결된 선
cv2.LINE_8 : 대각선을 포함한 8방향으로 연결된 선 (default)
cv2_LINE_AA : 부드러운 선 (anti=aliasing)
'''

img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (0, 255, 255) # BGR
THICKNESS = 3 # 두께

cv2.line(img, (50,100), (400, 50), COLOR, THICKNESS, cv2.LINE_8)
# 그릴 위치, 시작점, 끝 점, 색깔, 두께, 선 종류
cv2.line(img, (50,200), (400, 150), COLOR, THICKNESS, cv2.LINE_4)
cv2.line(img, (50,300), (400, 250), COLOR, THICKNESS, cv2.LINE_AA)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

##############
# 원
##############

img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (255, 255, 0) # BGR : 옥색
RADIUS = 50 # 반지름
THICKNESS = 10 # 두께

cv2.circle(img, (200, 100), RADIUS, COLOR, THICKNESS, cv2.LINE_AA) # 속이 빈 원
# 그릴 위치, 반지름, 색깔, 두께, 선 종류
cv2.circle(img, (400, 100), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA) # 속이 꽉 찬 원
# cv.FILLED 대신 -1도 가능

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

##############
# 사각형
##############

img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (0, 255, 0) # BGR : 초록색
THICKNESS = 3 # 두께

cv2.rectangle(img, (100, 100), (200,200), COLOR, THICKNESS) # 속이 빈 사각형
# 그릴 위치(왼쪽 위 좌표, 오른쪽 아래 좌표) ,색깔, 두께
cv2.rectangle(img, (300, 100), (400, 300), COLOR, -1) # 속이 꽉 찬 사각형
# -1 대신 cv.FILLED도 가능

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

##############
# 다각형
##############

img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (0, 0, 255) # BGR : 빨간색
THICKNESS = 3 # 두께

pts1 = np.array([[100, 100], [200, 100], [100, 200]]) # 좌표값 저장
pts2 = np.array([[200, 100], [300, 100], [300, 200]])

# cv2.polylines(img, [pts1], True, COLOR, THICKNESS, cv2.LINE_AA)
# cv2.polylines(img, [pts2], True, COLOR, THICKNESS, cv2.LINE_AA)
# 그릴 위치(리스트로 감쌈), 첫점과 끝점 연결 여부, 색깔, 두께

cv2.polylines(img, [pts1, pts2], True, COLOR, THICKNESS, cv2.LINE_AA)

pts3 = np.array([[[100, 300], [200, 300], [100,400]],[[200,300], [300, 300], [300, 400]]])
cv2.fillPoly(img, pts3, COLOR,cv2.LINE_AA) # 꽉 채울 수 있는 함수이므로 굳이 thickness, 연결 여부 등 필요 없음

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)