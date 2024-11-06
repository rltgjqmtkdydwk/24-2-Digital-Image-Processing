import numpy as np

def mat_access1(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            k = mat[i, j]       # 각각의 원소에 접근
            mat[i, j] = k * 2   # 2배 원소처리(그냥 mat*2 해도 됨)

def mat_access2(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            k = mat.item(i, j)
            mat.itemset((i, j), k * 2)

mat1 = np.arange(10).reshape(2, 5)
mat2 = np.arange(10).reshape(2, 5)

print("원소 처리 전: \n%s\n" % mat1)
mat_access1(mat1)
print("원소 처리 후: \n%s\n" % mat1)

print("원소 처리 전: \n%s\n" % mat2)
mat_access2(mat2)
print("원소 처리 후: \n%s\n" % mat2)
