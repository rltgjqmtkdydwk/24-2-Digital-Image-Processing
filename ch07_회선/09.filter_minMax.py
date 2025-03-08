import numpy as np, cv2

def minMax_filter(image, ksize, mode):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    center = ksize // 2

    for i in range (center, rows - center):       # 회선의 중심이 행 방향으로 이동하는
        for j in range(center, cols - center):    # 회선의 중심의 열 좌표
            # mask area
            y1, y2 = i - center, i + center + 1
            x1, x2 = j - center, j + center + 1
            mask = image[y1:y2, x1:x2]
            dst[i, j] = cv2.minMaxLoc(mask)[mode] # mode = 0 -> min / mode -> max
    return dst

image = cv2.imread("/Users/kslivergun/work1/class/24-2-digitalimage/ch07/img/min_max.jpg", cv2.IMREAD_GRAYSCALE)

miniFilter_img = minMax_filter(image, 3, 0)
maxiFilter_img = minMax_filter(image, 3, 1)

cv2.imshow("image", image)
cv2.imshow("miniFilter_img", miniFilter_img)
cv2.imshow("maxiFilter_img", maxiFilter_img)
cv2.waitKey(0)
