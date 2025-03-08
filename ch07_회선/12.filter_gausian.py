import numpy as np, cv2

image = cv2.imread("/Users/kslivergun/work1/class/24-2-digitalimage/ch07/img/smoothing.jpg", cv2.IMREAD_GRAYSCALE)

ksize = (5, 17)     # 가로*세로
gaussian_1dx = cv2.getGaussianKernel(ksize[1], 0, cv2.CV_32F)
gaussian_1dy = cv2.getGaussianKernel(ksize[0], 0, cv2.CV_32F)

gauss_img1 = cv2.GaussianBlur(image, ksize, 0)
gauss_img2 = cv2.sepFilter2D(image, -1, gaussian_1dx, gaussian_1dy)

titles = ['image', 'gauss_img1', 'gauss_img2']
[cv2.imshow(t, eval(t)) for t in titles]
cv2.waitKey(0)