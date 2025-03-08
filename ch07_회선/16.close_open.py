from fileinput import close
from pickletools import uint8
import numpy as np, cv2

image = cv2.imread("/Users/kslivergun/work1/class/24-2-digitalimage/ch07/img/morph.jpg", cv2.IMREAD_GRAYSCALE)
mask = np.array([[0,1,0], [1,1,1], [0,1,0]]).astype('uint8')
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]

open = cv2.morphologyEx(th_img, cv2.MORPH_OPEN, mask)
close = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask, iterations=1)

cv2.imshow('open', open)
cv2.imshow('close', close)
cv2.waitKey(0)