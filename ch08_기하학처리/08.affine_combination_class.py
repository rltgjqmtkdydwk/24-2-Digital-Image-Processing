# 어파인 변환의 연결
import cv2
import numpy as np

image = cv2.imread("img/affine2.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("image error")

# 이미지 크기 및 변수
size = image.shape[::-1]            # 이미지 크기
center = (size[0]//2, size[1]//2)   # 이미지 중심 좌표
angle = 45                          # 회전 각도
tr = (200, 0)                       # 평행 이동 값
scale_x, scale_y = 2.0, 1.5         # 크기 조정 비율 (확대 및 축소)

# 1. 중심 좌표 기준 회전 : 회전 변환과 크기 변경을 수행할 수 있는 어파인 행렬 반환
aff_mat1 = cv2.getRotationMatrix2D(center, angle, 1.0)

# 2. 크기 변경 - 확대 (scale_x 및 scale_y 적용)
aff_mat2 = np.array([
    [scale_x, 0, 0],
    [0, scale_y, 0]
], dtype=np.float32)

# 3. 회전 및 축소
aff_mat3 = cv2.getRotationMatrix2D(center, angle, 0.7).astype(np.float32)   # float형 변환

# 4. 복합 변환 (회전 + 축소 + 이동)
aff_mat4 = cv2.getRotationMatrix2D(center, angle, 0.7).astype(np.float32)   # float형 변환
aff_mat4[0, 0] *= scale_x
aff_mat4[1, 1] *= scale_y
aff_mat4[0, 2] += tr[0]
aff_mat4[1, 2] += tr[1]

# 입력영상에 어파인 변환 수행
dst1 = cv2.warpAffine(image, aff_mat1, size)
dst2 = cv2.warpAffine(image, aff_mat2, size)
dst3 = cv2.warpAffine(image, aff_mat3, size)
dst4 = cv2.warpAffine(image, aff_mat4, size)

cv2.imshow("image", image)
cv2.imshow("dst1_only_rotate", dst1)
cv2.imshow("dst2_only_scaling", dst2)
cv2.imshow("dst3_rotate_scaling", dst3)
cv2.imshow("dst4_rotate_scaling_translate", dst4)
cv2.waitKey(0)