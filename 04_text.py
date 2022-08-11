"""
04. 텍스트
"""

#######################################################

########################
# OpenCV에서 사용하는 글꼴 종류
########################

'''
cv2.FONT_HERSHEY_SIMPLEX : 보통 크기의 산 세리프 글꼴
cv2.FONT_HERSHEY_PLAIN : 작은 크기의 산 세리프 글꼴
cv2.FONT_HERSHEY_SCRIPT_SIMPLEX : 필기체 스타일 글꼴
cv2.FONT_HERSHEY_TRIPLEX : 보통 크기의 세리프 글꼴
cv2.FONT_ITALIC : 기울임 (다른 폰트와 함께 사용)
'''

import numpy as np
import cv2

img = np.zeros((480, 640, 3), dtype = np.uint8)

SCALE = 1 # 글자 크기
COLOR = (255, 255, 255) # 흰색
THICKNESS = 1 # 두께

cv2.putText(img, "Nado Simplex", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)
# 그릴 위치, 텍스트 내용, 시작 위치, 글꼴 종류, 크기, 색깔, 두께
cv2.putText(img, "Nado Plain", (20, 150), cv2.FONT_HERSHEY_PLAIN, SCALE, COLOR, THICKNESS)
cv2.putText(img, "Nado Script Simplex", (20, 250), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "Nado Triplex", (20, 350), cv2.FONT_HERSHEY_TRIPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "Nado Italic", (20, 450), cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC, SCALE, COLOR, THICKNESS)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


##############
# 한글 우회 방법
##############

import numpy as np
import cv2
# PIL (Python Image Library)
from PIL import ImageFont, ImageDraw, Image

img = np.zeros((480, 640, 3), dtype = np.uint8)

def myPutText(src, text, pos, font_size, font_color):
    img_pil  = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('fonts/gulim.ttc', font_size)
    draw.text(pos, txt, font=font, fill=font_color)
    return np.array(img_pil)

FONT_SIZE = 30 # 글자 크기
COLOR = (255, 255, 255) # 흰색

img = myPutText(img, "나도코딩", (20,50), FONT_SIZE, COLOR)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
