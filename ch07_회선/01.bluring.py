import numpy as np, cv2

# 회선 수행 함수 - 행렬 처리 방식(속도 면에서 유리)
def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)    # 회선 결과 저장 행렬
    ycenter, xcenter = rows//2, cols//2         # 마스크 중심 좌표

    for i in range(ycenter, rows-ycenter):      # 입력 행렬 반복 순회
        for j in range(xcenter, cols-xcenter):
            y1, y2 = i - ycenter, i+ycenter + 1
            x1, x2 = j - xcenter, j + xcenter + 1
            roi = image[y1:y2, x1:x2].astype("float32")
            temp = cv2.multiply(roi, mask)
            dst[i, j] = cv2.sumElems(temp)[0]
    return dst

# 회선 수행 함수 - 루프 처리 방식 (화소 직접 접근)
def filter2(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    ycenter, xcenter = rows//2, cols//2

    for i in range(ycenter, rows-ycenter):
        for j in range(xcenter, cols-xcenter):
            sum = 0.0
            for u in range(mask.shape[0]):       # 마스크 원소 반복 순회
                for v in range(mask.shape[1]):
                    y, x = i + u - ycenter, j + v - xcenter
                    sum += image[y, x] * mask[u, v]  # 화소 값과 마스크 원소 곱셈
            dst[i, j] = sum
    return dst

image = cv2.imread("images/filter_blur.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data = [ 1/9, 1/9, 1/9,
         1/9, 1/9, 1/9,
         1/9, 1/9, 1/9]
mask = np.array(data, np.float32).reshape(3, 3)

blur1 = filter(image, mask)
blur2 = filter2(image, mask)
blur1 = blur1.astype('uint8')
blur2 = cv2.convertScaleAbs(blur2)

cv2.imshow("image", image)
cv2.imshow("blur1", blur1)
cv2.imshow("blur2", blur2)
cv2.waitKey(0)