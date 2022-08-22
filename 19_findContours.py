"""
19. 이미지 검출 (윤곽선)
"""

#######################################################

# 윤곽선(Contour): 경계선을 연결한 선

import cv2

img = cv2.imread('card.png')
target_img = img.copy()  # 사본

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 애초에 이미지 불러올 때 grayscale로 설정해도 됨.

ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# threshold는 otsu가 알아서 설정해주므로, 값을 굳이 설정할 의미가 없음 : -1

# 윤곽선 검출 (findContours)
contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# 윤곽선 정보, 계층 구조
# = 이미지, 윤곽선 찾는 모드 (mode), 윤곽선 찾을때 사용하는 근사치 방법 (method)
# : CHAIN_APPROX_NONE, CHAIN_APPROX_SIMPLE

# 윤곽선 그리기 (drawContours)
COLOR = (0, 200, 0)  # 녹색
cv2.drawContours(target_img, contours, -1, COLOR, 2)
# 대상 이미지, 윤곽선 정보, 인덱스 (-1 이면 전체), 색깔, 두께

cv2.imshow('img', img)
cv2.imshow('gray', gray)  # 원본을 흑백으로 만든 이미지
cv2.imshow('otsu', otsu)  # 위의 흑백이미지를 otsu 알고리즘으로 이진화 한 이미지
cv2.imshow('contour', target_img)  # 위의 otsu를 통해 윤곽선을 찾아 그 정보대로 그린 이미지

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

#######################################################

###################
# 윤곽선 찾기 모드
###################

'''
cv2.RETR_EXTERNAL: 가장 외곽의 윤곽선만 찾음
cv2.RETR_LIST: 모든 윤곽선 찾음(계층 정보 없음)
cv2.RETR_TREE: 모든 윤곽선 찾음(계층 정보를 트리 구조로 생성)
'''

import cv2

img = cv2.imread('card.png')
target_img = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
contours, hierarchy = cv2.findContours(otsu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# contours, hierarchy = cv2.findContours(otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# print(hierarchy)
# print(f'총 발견 갯수 : {len(contours)}')

COLOR = (0, 200, 0)  # 녹색
cv2.drawContours(target_img, contours, -1, COLOR, 2)

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('otsu', otsu)
cv2.imshow('contour', target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

#######################################################

###################
# 경계 사각형
###################

# 윤곽선의 경계면을 둘러싸는 사각형(차후 얼굴 인식, 사물 인식 등에 사용 가능)
# boundingRect()

import cv2

img = cv2.imread('card.png')
target_img = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

COLOR = (0, 200, 0)

for cnt in contours:
    x, y, width, height = cv2.boundingRect(cnt)
    cv2.rectangle(target_img, (x, y), (x + width, y + height), COLOR, 2)  # 사각형 그림
    # 대상 이미지, 왼쪽 상단 좌표, 오른쪽 하단 좌표, 색상, 두께

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('otsu', otsu)
cv2.imshow('contour', target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

#######################################################

###################
# 면적
###################

# contourArea()

import cv2

img = cv2.imread('card.png')
target_img = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

COLOR = (0, 200, 0)

for cnt in contours:
    if cv2.contourArea(cnt) > 25000:
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img, (x, y), (x + width, y + height), COLOR, 2)  # 사각형 그림
# 모든 윤곽선의 경계면에 사각형을 생성하는게 아니라, 특정 사이즈 기준을 충족하는 경우만 생성
# 작은 사각형 없이 카드 기준으로만 생성하고 싶다면
# 카드의 면적 (가로 x 세로)을 계산해 contourArea를 적절히 지정해 주면 됨.

cv2.imshow('img', img)
cv2.imshow('contour', target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


#######################################################

'''
미니 프로젝트: 
    개별 카드 추출해서 파일 저장
'''

import cv2

img = cv2.imread('card.png')
target_img = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

COLOR = (0, 200, 0)

idx = 1
for cnt in contours:
    if cv2.contourArea(cnt) > 25000:
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img, (x, y), (x + width, y + height), COLOR, 2)  # 사각형 그림

        crop = img[y:y + height, x:x + width]  # 원본 이미지 중 찾은 윤곽선 크기(영역)만큼 crop에 저장
        cv2.imshow(f'card_crop_{idx}', crop)
        cv2.imwrite(f'card_crop_{idx}.png', crop)  # 파일 저장
        idx += 1

cv2.imshow('img', img)
cv2.imshow('contour', target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)