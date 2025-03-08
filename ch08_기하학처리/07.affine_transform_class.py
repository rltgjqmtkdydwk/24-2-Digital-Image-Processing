# 행렬 연산을 통한 기하학 변환 - 어파인 변환
import numpy as np, cv2

image = cv2.imread('img/affine.jpg', cv2.IMREAD_GRAYSCALE)

center = (200,200)
angle, scale = 30, 1
size = image.shape[::-1]

pt1 = np.array([(30,70),(20,240),(300,110)],np.float32)
pt2 = np.array([(120,20),(10,180),(280,260)],np.float32)

# cv2.getAffineTransform : 3개의 좌표쌍을 입력하면 어파인 변환 행렬을 반환한다.
aff_mat = cv2.getAffineTransform(pt1, pt2)
rot_mat = cv2.getRotationMatrix2D(center, angle, scale)

# cv2.warpAffine : 입력영상에 어파인 변환을 수행해서 반환한다.
dst3 =cv2.warpAffine(image, aff_mat, size, cv2.INTER_LINEAR)    # 양선형 보간(기본)
dst4 = cv2.warpAffine(image, rot_mat, size, cv2.INTER_LINEAR)   # 양선형 보간(기본)

image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
dst5 = cv2.cvtColor(dst3, cv2.COLOR_GRAY2BGR)

for i in range(len(pt1)):
    cv2.circle(image, tuple(pt1[i].astype(int)),3,(0,0,255),2)
    cv2.circle(dst3, tuple(pt2[i].astype(int)),3,(0,0,255),2)

cv2.imshow('image', image)
cv2.imshow('affine', dst3)
cv2.imshow("rotate", dst4)   
cv2.waitKey()