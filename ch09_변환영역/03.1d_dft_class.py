# 1차원 이산 푸리에 변환
import numpy as np, cv2
import matplotlib.pyplot as plt

fmax = 1000
dt = 1/fmax
t = np.arange(0, 1, dt)

# 주파수를 다르게 설정
g1 = np.sin(2 * np.pi * 50 * t)
g2 = np.sin(2 * np.pi * 120 * t)
g3 = np.sin(2 * np.pi * 260 * t)

g = g1 * 0.6 + g2 * 0.9 + g3 * 0.2

# openCV dft 함수
g_float32 = np.float32(g).reshape(-1, 1)
G_complex = cv2.dft(g_float32, flags=cv2.DFT_COMPLEX_OUTPUT)

# 계수(주파수의 강도) 계산
G_magnitude = cv2.magnitude(G_complex[:, 0, 0], G_complex[:, 0, 1])     # 실수부[0]와 허수부[1]의 제곱을 더해줘서 벡터로 나타낸다

# 역변환
g_reconstructed = cv2.idft(G_complex)
g_reconstructed = g_reconstructed[:, 0, 0]/len(g)   # 실수가 아닌 오차값 처리

N = len(g)
df = fmax/N
f = np.arange(0, N, df)

plt.figure(figsize=(10, 10))
plt.subplot(3, 1, 1), plt.plot(t[0:200], g[:200]), plt.title('Original Signal') 
plt.subplot(3, 1, 2), plt.plot(f[:N], G_magnitude[:N]), plt.title('DFT Amplitude Spectrum')
plt.subplot(3, 1, 3), plt.plot(t[0:200], g_reconstructed[:200]), plt.title('Reconstructed Signal')
plt.show()