from email.mime import image
import cv2

image = cv2.imread("/Users/kslivergun/work1/class/24-2-digitalimage/ch07/img/canny.jpg", cv2.IMREAD_GRAYSCALE)
canny = cv2.Canny(image, 100, 150) # src 하단 임계(T_low), 상단 임계(T_high)

cv2.imshow('image', image)
cv2.imshow('canny', canny)
cv2.waitKey(0)