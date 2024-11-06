import numpy as np, cv2

def print_rects(rects):
    print("-" * 46)                             	# 라인 출력
    print("사각형 원소\t 랜덤 사각형 정보\t  크기")
    print("-" * 46)
    for i, (x,y, w,h, a) in enumerate(rects):		# 사각형 데이터 출력
         print("rects[%i] = [(%3d,%3d) from (%3d,%3d)] %5d" %(i, x, y, w, h, a))
    

rands = np.zeros((5, 5), np.uint16)        		    # 5행 4열 행렬 생성
starts = cv2.randn(rands[:, :2 ], 100, 50)     		# 0~4행까지 시작좌표 랜덤 생성
ends = cv2.randn(rands[:, 2:-1], 300, 50)       	# 5~9행까지 종료좌표 랜덤 생성
sizes = cv2.absdiff(starts, ends)					# 시작좌표와 종료좌표간 차분 절대값 -> 크기
areas = sizes[:, 0] * sizes[:, 1]                   # 가로x세로 = 넓이
rects = rands.copy()                                # 결과 사각형으로 복사
rects[:, 2:-1] = sizes                              # 2열, 3열에 크기(가로, 세로) 저장
rects[:,-1] = areas                                 # 마지막(-1)열에 넓이 저장

idx = cv2.sortIdx(areas, cv2.SORT_EVERY_COLUMN).flatten()   # 정렬 인덱스

print_rects(rects)                      # 원본 사각형 정보 출력
print_rects(rects[idx.astype('int')])   # 크기순 정렬 사각형 출력