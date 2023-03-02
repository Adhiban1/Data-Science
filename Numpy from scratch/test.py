from Matrix import Matrix
from time import time
from CMatrix import CMatrix

start = time()
for i in range(1000):
    a = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    a = a.dot(a)
    a = 10*a
    a = a*a
    b = a.sum()
matrix_time = time()-start

start = time()
for i in range(1000):
    a = CMatrix([[1,2,3],[4,5,6],[7,8,9]])
    a = a.dot(a)
    a = 10*a
    a = a*a
    b = a.sum()
cmatrix_time = time()-start

print(f'cmatrix_time * {matrix_time/cmatrix_time} = matrix_time\nCMatrix is ~{matrix_time/cmatrix_time:.2f} times faster than Matrix')