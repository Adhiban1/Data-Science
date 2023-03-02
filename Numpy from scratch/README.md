# Matrix and CMatrix
- `Matrix` class - Made with Pure python
- `CMatrix` class - Made with Cython to optimize the performance

**Cython:**

Cython is a programming language, a superset of the Python programming language, designed to give C-like performance with code that is written mostly in Python with optional additional C-inspired syntax. Cython is a compiled language that is typically used to generate CPython extension modules.
# test.py
```python
from Matrix import Matrix, CMatrix
from time import time
import numpy as np
import pandas as pd

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

start = time()
for i in range(1000):
    a = np.array([[1,2,3],[4,5,6],[7,8,9]])
    a = a.dot(a)
    a = 10*a
    a = a*a
    b = a.sum()
numpy_time = time()-start

df = pd.DataFrame({'Name':['Matrix', 'CMatrix', 'Numpy'], 'Time Taken':[matrix_time, cmatrix_time, numpy_time]})
df = df.sort_values('Time Taken')
print(df)
```
run test.py in terminal
```python
python test.py
```
output:
```python
      Name  Time Taken
0  CMatrix    0.006224
1    Numpy    0.006896
2   Matrix    0.017838
```
**CMatrix is faster than or equal to Numpy.**