import cv2

'''
동영상 출력
'''

#######################################################

##############
# 1. 동영상 파일 출력
##############

cap = cv2.VideoCapture('video.mp4')

while cap.isOpened(): # 동영상 파일이 올바로 열렸는지?
    ret, frame = cap.read() # ret: 성공 여부, frame : 받아온 이미지 (프레임)
    if not ret :
        print('더 이상 가져올 프레임이 없어요')
        break
    cv2.imshow('video', frame)

    if cv2.waitKey(25) == ord('q'):
        # waitkey: 수치 조절하면, 동영상 재생 속도 조절됨.
        # key 값이 ord 함수 안의 값과 같으면, 종료

        print('사용자 입력에 의해 종료합니다.')
        break

cap.release() # 자원 해제
cv2.destroyAllWindows()
cv2.waitKey(1)

##############
# 2. 카메라 출력
##############

cap = cv2.VideoCapture(0)  # 0번째 카메라 장치

if not cap.isOpened():  # 카메라가 잘 열리지 않은 경우
    exit()  # 프로그램 종료

while True:  # 카메라가 열리면
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('camera', frame)
    if cv2.waitKey(1) == ord('q'):
        # 카메라의 경우 동영상의 끝이 없기 때문에, 사용자가 직접 q를 입력해야 종료됨.
        break

cap.release()  # 자원 해제
cv2.destroyAllWindows()
cv2.waitKey(1)

#######################################################