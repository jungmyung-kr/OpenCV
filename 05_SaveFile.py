"""
05. 파일 저장
"""

#######################################################

##############
# 이미지 저장
##############

import cv2
img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


################
# 저장 포맷 (jpg, png)
################

img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)  # 흑백으로 이미지 불러오기
cv2.imwrite('img_save.png', img)  # png 형태로 저장


##############
# 동영장 저장
##############

import cv2

cap = cv2.VideoCapture('video.mp4')

# 코덱 정의
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# four cc (character code) : 4글자 코드

# 프레임 크기, FPS
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 정수값으로 저장해야하므로 round함수 사용
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) * 2  # 원래 영상 재생 속도보다 2배 빨라짐

out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))
# 저장 파일명, 코덱, FPS, 크기(width, height)


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:  # return값이 false일 때
        break

    out.write(frame)
    # 받아온 값을 out에 지정한대로 저장함. (저장파일명, 코덱, 속도 등)
    # 영상 데이터만 처리 (소리 x)

    cv2.imshow('video', frame)  # video라는 이름으로 받아온 프레임 출력
    if cv2.waitKey(1) == ord('q'):
        break

out.release()  # 자원 해제 : 객체 사용을 위해 할당했던 하드웨어 및 소프트웨어 자원을 원래대로 되돌림
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)

'''
참고) 코덱 (codec)
: 영상 파일의 Encode, Decode를 처리함으로써 화면에서 영상을 보거나, 파일로 저장하는 작업을 도움

주로 사용하는 코덱
- MJPG
- DIVX
- H264 : 웹 브라우저용 비디오 코덱
'''