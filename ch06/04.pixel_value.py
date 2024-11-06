import cv2

image = cv2.imread("img/pixel.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")

(x,y),(w,h) = (180, 37), (15, 10)                   # 좌표는 x, y
roi_img = image[y:y+h, x:x+w]                       # 행렬 접근은 y, x

print("[roi_img] =")
for row in roi_img:
    for p in row:
        print("%4d" % p, end="")       # 순회 원소 하나씩 출력(행렬 원 하나 출력)
    print()