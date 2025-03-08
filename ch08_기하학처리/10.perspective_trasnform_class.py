# 원근 왜곡 보정
import numpy as np, cv2

image = cv2.imread('img/perspective.jpg', cv2.IMREAD_GRAYSCALE)

pts1 = np.float32([(80,40),(315,133),(75,300),(335,300)])   # 입력영상 4개 좌표
pts2 = np.float32([(50,60),(340,60),(50,320),(340,320)])    # 목적영상 4개 좌표

# 원근 변환 행렬
perspect_mat = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(image, perspect_mat, image.shape[1::-1],cv2.INTER_CUBIC)
print('[perspect_mat]=\n%s\n'%perspect_mat)

# 변환 좌표 계산
ones = np.ones((4,1), np.float64)
pts3 =np.append(pts1, ones, axis=1) # x,y 좌표 값에 1을 추가
pts4 = cv2.gemm(pts3, perspect_mat.T, 1, None, 1) # w값이 곱해진 상태

for i in range(len(pts4)):
    pts4[i] /= pts4[i][2]
    cv2.circle(image, tuple(pts1[i].astype(int)),4,(0,255,0),-1)
    cv2.circle(dst, tuple(pts2[i].astype(int)),4,(0,255,0),-1)
cv2.imshow('image', image)
cv2.imshow('perspective', dst)
cv2.waitKey(0)
