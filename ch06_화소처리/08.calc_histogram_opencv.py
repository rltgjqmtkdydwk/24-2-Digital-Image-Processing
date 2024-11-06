import numpy as np, cv2

def calc_histo(image, histSize, ranges=[0, 256] ):   # 행렬 원소의 1차원 히스토그램
    hist = np.zeros((histSize, 1), np.float32)          # 히스토그램 누적 행렬
    gap = ranges[1] / histSize                          # 계급 간격

    for i in (image/gap).flat:                      # 2차원 행렬 순회 방식
            hist[int(i)]+= 1
    return hist

image = cv2.imread("img/pixel.jpg", cv2.IMREAD_GRAYSCALE)   # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 발생")

histSize, ranges = [32], [0, 256]                       # 히스토그램 간격수, 값 범위
gap = ranges[1]/histSize[0]                             # 계급 간격
ranges_gap = np.arange(0, ranges[1]+1, gap)             # numpy 계급범위, 간격
hist1 = calc_histo(image, histSize, ranges)                       # User 함수
hist2 = cv2.calcHist([image], [0], None, histSize, ranges)        # OpenCV 함수
hist3, bins = np.histogram(image, ranges_gap)                     # numpy 함수

print("User 함수: \n", hist1.flatten())                           # 행렬을 벡터로 변환하여 출력
print("OpenCV 함수: \n", hist2.flatten())
print("numpy 함수 \n", hist3)