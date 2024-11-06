import numpy as np
import cv2 as cv

image = np.zeros((200, 400), np.uint8)      # 영행렬 생성
image[:] = 200                              # 슬라이스 연산자로 행렬 원소값 지정

title1, title2 = 'Position1', 'Position2'
cv.namedWindow(title1, cv.WINDOW_AUTOSIZE)  # namedWindow() : 윈도우 생성 및 이름 지정
cv.namedWindow(title2)
cv.moveWindow(title1, 150, 150)             # moveWindow() : 윈도우 이동 및 위치 지정
cv.moveWindow(title1, 400, 50)

cv.imshow(title1, image)                    # imshow() : 행렬 원소를 영상으로 표시
cv.imshow(title2, image)
cv.waitKey(0)                               # waitKey() : 키 이벤트 대기
cv.destroyAllWindows()                      # destroyAllWindows() : 열린 모든 윈도우 파괴