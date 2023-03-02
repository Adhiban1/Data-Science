# Matrix and CMatrix
- `Matrix` class - Made with Pure python
- `CMatrix` class - Made with Cython to optimize the performance

**Cython:**

Cython is a programming language, a superset of the Python programming language, designed to give C-like performance with code that is written mostly in Python with optional additional C-inspired syntax. Cython is a compiled language that is typically used to generate CPython extension modules.
# test.py
```python
from Matrix import Matrix, CMatrix
from time import time

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
```
run test.py in terminal
```python
python test.py
```
output:
```python
cmatrix_time * 3.464074819947435 = matrix_time
CMatrix is ~3.46 times faster than Matrix
```