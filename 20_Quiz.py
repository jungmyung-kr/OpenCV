"""
20. 퀴즈
"""

#######################################################

'''
OpenCV를 이용하여 가로로 촬영된 동영상을 세로로 회전하는 프로그램을 작성하시오

조건
회전: 시계 반대방향으로 90도
재생속도(FPS): 원본x4배
출력 파일명: city_output.avi(코덱: DIVX)
원본 파일명: city.mp4
'''

import cv2

cap = cv2.VideoCapture('city.mp4')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('city_output.avi', fourcc, fps * 4, (height, width))
# 90도 회전하면서 가로, 세로 사이즈가 바뀌어야 하므로, 순서 바꿔서 (height, width)로 기재

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rotate_frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)  # 시계 반대 방향으로 90도
    out.write(rotate_frame)
    cv2.imshow('city', frame)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)