# 이산 코사인 변환
import numpy as np, cv2

block = np.zeros((8,8), np.uint8)   # 블럭을 만들어서 각각을 계산
cv2.randn(block, 128, 50)
dct4 = cv2.dct(block.astype('float32'))
idct4 = cv2.dct(dct4, flags=cv2.DCT_INVERSE)

print('block=\n', block)
print('dct4=\n', dct4)
print('idct4=\n', cv2.convertScaleAbs(idct4))
