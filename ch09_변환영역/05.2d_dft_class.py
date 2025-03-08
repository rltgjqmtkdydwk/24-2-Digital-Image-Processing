# 고속 푸리에 변환
import numpy as np, cv2

def calc_specturm(complex):
    dst = cv2.magnitude(complex[:, :, 0], complex[:, :, 1])
    dst = cv2.log(dst + 1)
    cv2.normalize(dst, dst, 0, 255, cv2.NORM_MINMAX)
    return cv2.convertScaleAbs(dst)

image = cv2.imread("img/dft_240.jpg", cv2.IMREAD_GRAYSCALE)
image_float = np.float32(image)
dft = cv2.dft(image_float, flags=cv2.DFT_COMPLEX_OUTPUT)

spectrum1 = calc_specturm(dft)
spectrum2 = np.fft.fftshift(spectrum1)
# re_image = cv2.idft(dft, flags=cv2.DFT_SCALE[:, :, 0])
re_image = cv2.idft(dft, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
cv2.normalize(re_image, re_image, 0, 255, cv2.NORM_MINMAX)
re_image = np.uint8(re_image)

cv2.imshow('image', image)
cv2.imshow('spectrum1', spectrum1)
cv2.imshow('spectrum2', spectrum2)
cv2.imshow('re_image', re_image)
cv2.waitKey(0)