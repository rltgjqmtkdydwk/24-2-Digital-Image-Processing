# 이산 코사인 변환 - DCT를 이용한 주파수 영역 필터링
import numpy as np, cv2

def dct_filtering(img, filter, M, N):
    dst = np.empty(img.shape, np.float32)
    for i in range(0, img.shape[0], M):
        for j in range(0, img.shape[1], N):
            block = img[i:i+M, j:j+N]
            dct_block = cv2.dct(block.astype('float32'))
            dct_block = dct_block * filter
            dst[i:i+M, j:j+N] = cv2.dct(dct_block, flags=cv2.DCT_INVERSE)   # 선택한 블럭으로 원래 이미지 구성
    return cv2.convertScaleAbs(dst)

image = cv2.imread('img/dct.jpg', cv2.IMREAD_GRAYSCALE)

M, N = 8, 8
filters = [np.zeros((M,N), np.float32) for i in range(5)]
titles = ['DC Pass', 'High Pass', 'Low Pass', 'Vertical Pass', 'Horizontal Pass']

filters[0][0,0] = 1
filters[1][:], filters[1][0,0] = 1, 0   # High Pass
filters[2][:M//2, :N//2] = 1    # Low Pass
filters[3][0,1:] = 1    # Vertical Pass : 수직으로 나타나는 패턴만 살림
filters[4][1:,0] = 1    #Horizontal Pass : 수평으로 나타나는 패턴만 살림

for filter, title in zip(filters, titles):
    dst = dct_filtering(image, filter, M, N)
    cv2.imshow(title, dst)

cv2.imshow('image', image)
cv2.waitKey(0)