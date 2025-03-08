import numpy as np, cv2
from Common.filters import differential

def diffrential(image, data1, data2):
    # 프리윗 마스크 생성
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)
    
    # 수직, 수평 방향 에지 검출
    dst1 = filter(image, mask1)
    dst2 = filter(image, mask2)
    
    # 절대값 변환
    dst1, dst2 = np.abs(dst1), np.abs(dst2)
    
    # 에지 강도 계산
    dst = cv2.magnitude(dst1, dst2)
    
    # 값 범위 조정 및 타입 변환
    dst = np.clip(dst, 0, 255).astype('uint8')
    dst1 = np.clip(dst1, 0, 255).astype('uint8')
    dst2 = np.clip(dst2, 0, 255).astype('uint8')
    
    return dst, dst1, dst2

image = cv2.imread("image/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [-1, 0, 1, 
        -1, 0, 1, 
        -1, 0, 1]
data2 = [-1, -1, -1, 
        0, 0, 0, 
        1, 1, 1]

dst, dst1, dst2 = differential(image, data1, data2)

cv2.imshow('image', image)
cv2.imshow('edge', dst)
cv2.imshow('dst1',dst1) # 왼쪽 대각선에서 봤을 때의 변화
cv2.imshow('dst2', dst2) # 오른쪽 대각선에서 봤을 때의 변화

cv2.waitKey(0)