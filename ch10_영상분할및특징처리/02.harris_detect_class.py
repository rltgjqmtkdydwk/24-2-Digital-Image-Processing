import numpy as np, cv2

def draw_corner(corner, image, thresh):
    corner = cv2.normalize(corner, 0, 300, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    pts = np.where(corner > thresh)
    corners, (h,w) = [], corner.shape
    for i, j in np.transpose(pts):
        if 0 < i < h-1 and 0 < j < w-1:
            neighbor = corner[i-1:i+2, j-1:j+2].flatten()
            max = np.max(neighbor)
            if corner[i,j] >= max:
                corners.append((j,i))
    for pt in corners:
        cv2.circle(image, pt, 3, (0, 230, 0), -1)

    print('임계값: %2d, 코너개수: %2d' %(thresh, len(corners)))
    return image

def onCornerHarris(thresh):
    img2 = draw_corner(corner2, np.copy(image), thresh)
    dst = img2
    cv2.imshow('Harris Detect', dst)

image = cv2.imread('img/harris.jpg', cv2.IMREAD_COLOR)

blocksize = 4
apentureSize = 3 # sobel mask size
k = 0.04    # 행렬의 대각합에 곱해지는 가중치
thresh = 2
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
corner2 = cv2.cornerHarris(gray, blocksize, apentureSize, k)
onCornerHarris(thresh)

cv2.createTrackbar('Threshold', 'Harris Detect', thresh, 20, onCornerHarris)
cv2.waitKey(0)