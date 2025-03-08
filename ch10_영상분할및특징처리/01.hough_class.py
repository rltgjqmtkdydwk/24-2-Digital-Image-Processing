import numpy as np, cv2, math

def draw_houghlines(src, lines, nline):
    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
    min_length = min(len(lines), nline)

    for i in range(min_length):
        rho, radian = lines[i, 0, 0:2]
        a, b = math.cos(radian), math.sin(radian)
        pt = (a * rho, b * rho)
        delta = (-1000*b, 1000*a)
        pt1 = np.add(pt, delta).astype('int')
        pt2 = np.subtract(pt, delta).astype('int')
        cv2.line(dst, tuple(pt1), tuple(pt2), (0, 255, 0), 2, cv2.LINE_AA)

    return dst

img = cv2.imread("img/hough.jpg")

# edge
blur = cv2.GaussianBlur(img, (5,5), 2, 2)
canny = cv2.Canny(blur,  100, 200, 5)
rho, theta = 1, np.pi/100
lines2 = cv2.HoughLines(canny, rho, theta, 80)
dst2 = draw_houghlines(canny, lines2, 7)

cv2.imshow("image", img)
cv2.imshow("canny", canny)
cv2.imshow("detected lines", dst2)
cv2.waitKey(0)