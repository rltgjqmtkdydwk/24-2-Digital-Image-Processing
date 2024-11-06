import numpy as np, cv2

def draw_histo(hist, shape=(200, 256)):                    # 색상 팔레트 생성
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)    # 정규화
    gap = hist_img.shape[1] / hist.shape[0]  # 한 계급 크기
    
    for i, h in enumerate(hist):
        x = int(round(i * gap))
        w = int(round(gap))
        cv2.rectangle(hist_img, (x,0,w, int(h) ), 0, cv2.FILLED) # 팔레트 색으로 그리기

    return cv2.flip(hist_img, 0)
