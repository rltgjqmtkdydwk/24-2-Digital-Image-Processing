import numpy as np, cv2, time

def pixel_access1(image):
    image1 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i, j]
            image[i, j] = 255 - pixel       # 흑백반전 : 0(검은색)~255(밝은색)
    return image1

def pixel_access2(image):
    image2 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image.item(i, j)
            image.itemset((i, j), 256 - pixel)
    return image2

def pixel_access3(image):
    lut = [255 - i for i in range(256)]     # lut = [255, 254, ... , 0]
    lut = np.array(lut, np.unit8)           # image의 화소로 index 처리
    image3 = lut[image]
    return image3

def pixel_access4(image):
    image4 = cv2.subtract(255, image)
    return image4

def pixel_access5(image):
    image5 = 255 - image        # 행렬간계산 : 각각의 원소를 255에서 빼는 계산
    return image5

image = cv2.imread("/Users/kslivergun/work1/class/24-2-digitalimage/ch05/img/logo.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

image1 = time_check(pixel_access1, "[방법1] 직접접근방식 수행시간")
image2 = time_check(pixel_access2, "[방법2] item()함수방식 수행시간")
image3 = time_check(pixel_access3, "[방법3] 룩업테이블방식 수행시간")
image4 = time_check(pixel_access4, "[방법4] openCV함수방식 수행시간")
image5 = time_check(pixel_access5, "[방법5] ndarray연산방식 수행시간")
