# 가우시안, 버터워스 필터링
import numpy as np, cv2
import matplotlib.pyplot as plt                     # 그래프 그리기
from mpl_toolkits.mplot3d import Axes3D             # 3차원 그래프 라이브러리

def get_gaussianFilter(shape, R):
    u = np.array(shape)//2
    y = np.arange(-u[0], u[0], 1)
    x = np.arange(-u[1], u[1], 1)
    x, y = np.meshgrid(x, y)
    filter = np.exp(-(x**2 + y**2)/ (2 * R**2))
    return x, y, filter if len(shape) < 3 else cv2.merge([filter, filter])

def get_butterworthFilter(shape, R, n):
    u = np.array(shape)//2
    y = np.arange(-u[0], u[0], 1)
    x = np.arange(-u[1], u[1], 1)
    x, y = np.meshgrid(x, y)
    dist = np.sqrt(x**2 + y**2)
    filter = 1 / (1 + np.power(dist / R, 2 * n))
    return x, y, filter if len(shape) < 3 else cv2.merge([filter, filter])

image = cv2.imread('img/filter.jpg', cv2.IMREAD_GRAYSCALE)
image = np.float32(image)

dft = cv2.dft(image, flags=cv2.DFT_COMPLEX_OUTPUT)    # 푸리에 변환 (복소수 출력)
dft = np.fft.fftshift(dft)          # 셔플링
spectrum = np.abs(dft)              # 주파수 성분의 크기 계산
x1, y1, gauss_filter = get_gaussianFilter(dft.shape, 30)    # filter 생성
x2, y2, butter_filter = get_butterworthFilter(dft.shape, 30, 10)

filtered_dft1 = dft * gauss_filter
filtered_dft2 = dft * butter_filter
gauss_img = cv2.idft(filtered_dft1, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)  # 역푸리에 변환
butter_img = cv2.idft(filtered_dft2, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
spectrum1 = np.abs(filtered_dft1)       # 필터링 후 스펙트럼 계산
spectrum2 = np.abs(filtered_dft2)

plt.figure(figsize=(10,10))

ax1 = plt.subplot(332, projection='3d') # 3차원 그래프
ax1.plot_surface(x1, y1, gauss_filter, cmap='RdPu')
plt.title("gauss_filter")
ax2 = plt.subplot(333, projection='3d')
ax2.plot_surface(x2, y2, butter_filter, cmap='RdPu')
plt.title("butter_filter")

titles = ['input image', 'gauss_lowpassed_image', 'butter_lowpassed_image', 
        'input spectrum', 'gauss_lowpassed_spectrum', 'butter_lowpassed_spectrum']
images = [image, gauss_img, butter_img, spectrum, spectrum1, spectrum2]
plt.gray()
for i, t in enumerate(titles):
    plt.subplot(3, 3, i+4)
    plt.imshow(images[i])
    plt.title(t)
plt.tight_layout(), plt.show()
