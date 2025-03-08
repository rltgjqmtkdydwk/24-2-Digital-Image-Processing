import numpy as np, cv2

def median_filter(image, ksize):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    center = ksize // 2

    for i in range (center, rows - center):    
        for j in range(center, cols - center):
            # mask area
            y1, y2 = i - center, i + center + 1
            x1, x2 = j - center, j + center + 1
            mask = image[y1:y2, x1:x2].flatten()

            sort_mask = np.sort(mask)
            median_idx = len(sort_mask) // 2
            dst[i, j] = sort_mask[median_idx]
            # sort_mask = cv2.sort(mask, cv2.SORT_EVERY_COLUMN)
            # dst[i, j] = int(sort_mask)[sort_mask.size/2].item()
    return dst

def salt_pepper_noise(img, n):  # 이미지랑 같은 크기로 인덱스
    h, w = img.shape[:2]
    x, y = np.random.randint(0, w, n), np.random.randint(0, h, n)
    noise = img.copy()
    for (x,y) in zip(x,y):
        noise[y, x] = 0 if np.random.rand() < 0.5 else 255
    return noise

image = cv2.imread("/Users/kslivergun/work1/class/24-2-digitalimage/ch07/img/median.jpg", cv2.IMREAD_GRAYSCALE)

noise = salt_pepper_noise(image, 500)
med_img1 = median_filter(noise, 5)
med_img2 = cv2.medianBlur(noise, 5)

cv2.imshow("image", image)
cv2.imshow("noise", noise)
cv2.imshow("med_img1", med_img1)
cv2.imshow("med_img2", med_img2)
cv2.waitKey(0)
