import matplotlib.pyplot as plt
import numpy as np

methods = ['none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36' ] # 보간법 적용
grid = np.random.rand(5, 5) # 0 ~ 1 사이의 임의 난수

fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(8, 6)) #  서브 플롯 새성

for ax, method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=method, cmap='gray') # 명암도 영상 표시
    ax.set_title(method)
plt.tight_layout(), plt.show()
