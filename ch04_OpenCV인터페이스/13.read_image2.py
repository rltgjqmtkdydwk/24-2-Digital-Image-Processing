import cv2
from matplotlib import pyplot as plt

def print_matInfo(name, image):
    if image.dtype == 'uint8':     mat_type = "CV_8U"
    elif image.dtype == 'int8':    mat_type = "CV_8S"
    elif image.dtype == 'uint16':  mat_type = "CV_16U"
    elif image.dtype == 'int16':   mat_type = "CV_16S"
    elif image.dtype == 'float32': mat_type = "CV_32F"
    elif image.dtype == 'float64': mat_type = "CV_64F"
    nchannel = 3 if image.ndim == 3 else 1

    ## depth, channel 출력
    print("%12s: depth(%s), channels(%s) -> mat_type(%sC%d)"
          % (name, image.dtype, nchannel, mat_type,  nchannel))

title1, title2 = "color2gray", "color2color"
color2gray = cv2.imread("img/read_color.jpg", cv2.IMREAD_GRAYSCALE)
color2color = cv2.imread("img/read_color.jpg", cv2.IMREAD_COLOR)

if color2gray is None or color2color is None:
    raise Exception("영상 파일 읽기 에러")

print("행렬 좌표 (100, 100) 화소값")
print("%s %s" % (title1, color2gray[100, 100]))     # 한 화소값 표시
print("%s %s\n" % (title2, color2color[100, 100]))

print_matInfo(title1, color2gray)                   # 행렬 정보 출력
print_matInfo(title2, color2color)

r, g, b = cv2.split(color2color)
color2color2 = cv2.merge([r, g, b])
plt.imshow(color2color)
plt.xticks([])  
plt.yticks([]) 
plt.show()

cv2.imshow(title1, color2gray)                      
cv2.imshow(title2, color2color)
cv2.waitKey(0)