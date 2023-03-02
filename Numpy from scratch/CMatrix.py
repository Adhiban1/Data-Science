import random
from CMatrixLib import *

class CMatrix:
    def __init__(self, l):
        self.list = l
        self.shape = (len(l), len(l[0]))

        for i in l:
            if len(i) != self.shape[1]:
                raise Exception('CMatrix shape error')

    def __repr__(self):
        return self.list

    def __str__(self):
        return '\n'.join([str(i) for i in self.list])

    def __add__(self, other):
        if type(other) == CMatrix :
            if self.shape == other.shape:
                temp = matrixAdd(self.list, other.list, self.shape[0], self.shape[1])
                return CMatrix(temp)
            else:
                raise Exception('Shape must be equal')
        else:
            temp = [[self.list[i][j] + other for j in range(self.shape[1])] for i in range(self.shape[0])]
            temp = matrixAdd_s(self.list, other, self.shape[0], self.shape[1])
            return CMatrix(temp) 

    def __radd__(self, other):
        if type(other) == CMatrix :
            pass
        else:
            temp = matrixAdd_s(self.list, other, self.shape[0], self.shape[1])
            return CMatrix(temp)

    def __sub__(self, other):
        if type(other) == CMatrix :
            if self.shape == other.shape:
                temp = matrixSub(self.list, other.list, self.shape[0], self.shape[1])
                return CMatrix(temp)
            else:
                raise Exception('Shape must be equal')
        else:
            temp = matrixSub_s(self.list, other, self.shape[0], self.shape[1])
            return CMatrix(temp)

    def __rsub__(self, other):
        if type(other) == CMatrix :
            pass
        else:
            temp = matrixSub_s(self.list, other, self.shape[0], self.shape[1])
            return CMatrix(temp)

    def __mul__(self, other):
        if type(other) == CMatrix :
            if self.shape == other.shape:
                temp = matrixMul(self.list, other.list, self.shape[0], self.shape[1])
                return CMatrix(temp)
            else:
                raise Exception('Shape must be equal')
        else:
            temp = matrixMul_s(self.list, other, self.shape[0], self.shape[1])
            return CMatrix(temp)
    
    def __rmul__(self, other):
        if type(other) == CMatrix :
            pass
        else:
            temp = matrixMul_s(self.list, other, self.shape[0], self.shape[1])
            return CMatrix(temp)
    
    def __div__(self, other):
        if type(other) == CMatrix :
            if self.shape == other.shape:
                temp = matrixDiv(self.list, other.list, self.shape[0], self.shape[1])
                return CMatrix(temp)
            else:
                raise Exception('Shape must be equal')
        else:
            temp = matrixDiv_s(self.list, other, self.shape[0], self.shape[1])
            return CMatrix(temp)
    
    def __rdiv__(self, other):
        if type(other) == CMatrix :
            pass
        else:
            temp = matrixDiv_s(self.list, other, self.shape[0], self.shape[1])
            return CMatrix(temp)
    
    def __floordiv__(self, other):
        if type(other) == CMatrix :
            if self.shape == other.shape:
                temp = matrixFloorDiv(self.list, other.list, self.shape[0], self.shape[1])
                return CMatrix(temp)
            else:
                raise Exception('Shape must be equal')
        else:
            temp = matrixFloorDiv_s(self.list, other, self.shape[0], self.shape[1])
            return CMatrix(temp)
    
    def __rfloordiv__(self, other):
        if type(other) == CMatrix :
            pass
        else:
            temp = matrixFloorDiv_s(self.list, other, self.shape[0], self.shape[1])
            return CMatrix(temp)

    def dot(self, other):
        if self.shape[1] == other.shape[0]:
            temp = dot(self.list, other.list, self.shape[0], self.shape[1], other.shape[1])
            return CMatrix(temp)
        else:
            raise Exception(f'Shape not compatible for dot product')

    def sum(self):
        return sum([sum(i) for i in self.list])

def randIntCMatrix(i, j, s, e):
    temp = [[random.randint(s,e) for _ in range(j)] for _ in range(i)]
    return CMatrix(temp)