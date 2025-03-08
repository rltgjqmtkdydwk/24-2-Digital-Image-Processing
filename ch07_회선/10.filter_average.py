import numpy as np, cv2

def average_filter(image, ksize):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    center = ksize // 2

    for i in range (center, rows - center):
        for j in range(center, cols - center):
            # mask area
            y1, y2 = i - center, i + center + 1
            x1, x2 = j - center, j + center + 1
            if y1 < 0 or y2 > rows or x1 < 0 or x2 > cols:
                dst[i, j] = image[i, j]
            else:
                mask = image[y1:y2, x1:x2]
                dst[i, j] = cv2.mean(mask)[0]
    return dst

image = cv2.imread("/Users/kslivergun/work1/class/24-2-digitalimage/ch07/img/filter_avg.jpg", cv2.IMREAD_GRAYSCALE)

avg_img = average_filter(image, 5)
blur_img = cv2.blur(image, (5,5), cv2.BORDER_REFLECT)

cv2.imshow("image", image)
cv2.imshow("avg_img", avg_img)
cv2.imshow("blur_img", blur_img)
cv2.waitKey(0)
