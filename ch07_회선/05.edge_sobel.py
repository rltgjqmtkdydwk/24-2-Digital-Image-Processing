import numpy as np, cv2
from Common.filters import differential

# def differential(image, data1, data2):
#     mask1 =np.array(data1, np.float32).reshape(3,3)
#     mask2 = np.array(data2, np.float32).reshape(3,3)

#     dst1 = filter(image, mask1)
#     dst2 = filter(image, mask2)

#     dst1, dst2 = np.abs(dst1), np.abs(dst2)
#     dst = cv2.magnitude(dst1, dst2) # Gradient magnitude

#     dst = np.clip(dst, 0 , 255).astype('uint8') # cv2.covertScaleAbs(dst) value<0 -> 0 value >255 -> 255
#     dst1 = np.clip(dst1, 0, 255).astype('uint8')
#     dst2 = np.clip(dst2, 0, 255).astype('uint8')
    
#     return dst, dst1, dst2

image = cv2.imread("image/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [-1, 0, 1, 
        -2, 0, 2, 
        -1, 0, 1]
data2 = [-1, -2, -1, 
        0, 0, 0, 
        1, 2, 1]
dst, dst1, dst2 = differential(image, data1, data2)

# OpenCV 제공 소벨 예지 계산
dst3 = cv2.Sobel(np.float32(image), cv2.CV_32F,1,0,3)
dst4 = cv2.Sobel(np.float32(image), cv2.CV_32F,0,1,3)
dst3 = cv2.convertScaleAbs(dst3)
dst4 = cv2.convertScaleAbs(dst4)

cv2.imshow('dst1',dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3',dst3)
cv2.imshow('dst4', dst4)

cv2.waitKey(0)

