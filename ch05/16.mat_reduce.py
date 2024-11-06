import numpy as np, cv2
m = np.random.rand(3, 5) * 1000//10     # 3행, 5열 0~1 사이 실수인 난수(0~99) 생성

reduce_sum = cv2.reduce(m, dim=0, rtype=cv2.REDUCE_SUM)     # 0 - 열방향 축소
reduce_avg = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_AVG)     # 1 - 행방향 축소
reduce_max = cv2.reduce(m, dim=0, rtype=cv2.REDUCE_MAX)
reduce_min = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_MIN)

print("[m1] = \n%s\n" %m)
print("[m_reduce_sum] =", reduce_sum.flatten())             # 1차원 벡터로 출력
print("[m_reduce_avg] =", reduce_avg.flatten())
print("[m_reduce_max] =", reduce_max.flatten())
print("[m_reduce_min] =", reduce_min.flatten())