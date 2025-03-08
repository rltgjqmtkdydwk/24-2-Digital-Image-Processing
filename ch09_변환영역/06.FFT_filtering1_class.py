# 저주파 및 고주파 통과 필터링
import numpy as np, cv2

def calc_specturm(complex):
    dst = cv2.magnitude(complex[:, :, 0], complex[:, :, 1])
    dst = cv2.log(dst + 1)
    cv2.normalize(dst, dst, 0, 255, cv2.NORM_MINMAX)
    return cv2.convertScaleAbs(dst)

image = cv2.imread('img/filter.jpg', cv2.IMREAD_GRAYSCALE)

cy, cx = np.divmod(image.shape, 2)[0]

dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
specturm = calc_specturm(np.fft.fftshift(dft))

lowpass = np.zeros(dft.shape, np.float32)
highpass = np.ones(dft.shape, np.float32)

cv2.circle(lowpass, (cx, cy), 30, (1,1), -1)
cv2.circle(highpass, (cx, cy), 30, (0,0), -1)

lowpassed_dft = np.fft.fftshift(dft) * lowpass
highpassed_dft = np.fft.fftshift(dft) * highpass

lowpassed_image = cv2.convertScaleAbs(
    cv2.idft(np.fft.fftshift(lowpassed_dft), 
    flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT))

highpassed_image = cv2.convertScaleAbs(
    cv2.idft(np.fft.fftshift(highpassed_dft), 
    flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT))

cv2.imshow('image', image)
cv2.imshow('lowpassed_image', lowpassed_image)
cv2.imshow('highpassed_image', highpassed_image)
cv2.imshow('spectrum', specturm)
cv2.imshow('lowpassed_spec', calc_specturm(lowpassed_dft))
cv2.imshow('highpassed_spec', calc_specturm(highpassed_dft))
cv2.waitKey(0)
