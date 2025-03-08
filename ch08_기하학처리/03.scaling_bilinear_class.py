# 양선형 보간법
import numpy as np, cv2

image = cv2.imread('img/interpolation.jpg', cv2.IMREAD_GRAYSCALE)

size = (350, 400)
dst3 = cv2.resize(image, size, 0, 0, cv2.INTER_LINEAR)  # 양선형 보간법 : 경계부분 계단현상
dst4 = cv2.resize(image, size, 0, 0, cv2.INTER_NEAREST) # 최근접 이웃 보간법 : 중간 화소 값으로 계산

cv2.imshow('image', image)
cv2.imshow('bilinear', dst3)
cv2.imshow('nearest',dst4)
cv2.waitKey(0)
