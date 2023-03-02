import random

class Matrix:
    def __init__(self, l):
        self.list = l
        self.shape = (len(l), len(l[0]))

        for i in l:
            if len(i) != self.shape[1]:
                raise Exception('Matrix shape error')

    def __repr__(self):
        return self.list

    def __str__(self):
        return '\n'.join([str(i) for i in self.list])

    def __add__(self, other):
        if type(other) == Matrix :
            if self.shape == other.shape:
                temp = [[self.list[i][j] + other.list[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
                return Matrix(temp)
            else:
                raise Exception('Shape must be equal')
        else:
            temp = [[self.list[i][j] + other for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Matrix(temp) 

    def __radd__(self, other):
        if type(other) == Matrix :
            pass
        else:
            temp = [[self.list[i][j] + other for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Matrix(temp)

    def __sub__(self, other):
        if type(other) == Matrix :
            if self.shape == other.shape:
                temp = [[self.list[i][j] - other.list[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
                return Matrix(temp)
            else:
                raise Exception('Shape must be equal')
        else:
            temp = [[self.list[i][j] - other for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Matrix(temp)

    def __rsub__(self, other):
        if type(other) == Matrix :
            pass
        else:
            temp = [[self.list[i][j] - other for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Matrix(temp)

    def __mul__(self, other):
        if type(other) == Matrix :
            if self.shape == other.shape:
                temp = [[self.list[i][j] * other.list[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
                return Matrix(temp)
            else:
                raise Exception('Shape must be equal')
        else:
            temp = [[self.list[i][j] * other for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Matrix(temp)
    
    def __rmul__(self, other):
        if type(other) == Matrix :
            pass
        else:
            temp = [[self.list[i][j] * other for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Matrix(temp)
    
    def __div__(self, other):
        if type(other) == Matrix :
            if self.shape == other.shape:
                temp = [[self.list[i][j] / other.list[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
                return Matrix(temp)
            else:
                raise Exception('Shape must be equal')
        else:
            temp = [[self.list[i][j] / other for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Matrix(temp)
    
    def __rdiv__(self, other):
        if type(other) == Matrix :
            pass
        else:
            temp = [[self.list[i][j] / other for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Matrix(temp)
    
    def __floordiv__(self, other):
        if type(other) == Matrix :
            if self.shape == other.shape:
                temp = [[self.list[i][j] // other.list[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
                return Matrix(temp)
            else:
                raise Exception('Shape must be equal')
        else:
            temp = [[self.list[i][j] // other for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Matrix(temp)
    
    def __rfloordiv__(self, other):
        if type(other) == Matrix :
            pass
        else:
            temp = [[self.list[i][j] // other for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Matrix(temp)
    
    def dot(self, other):
        if self.shape[1] == other.shape[0]:
            temp = [[0 for _ in range(other.shape[1])] for _ in range(self.shape[0])]
            for i in range(self.shape[0]):
                for k in range(other.shape[1]):
                    for j in range(self.shape[1]):
                        temp[i][k] += self.list[i][j] * other.list[j][k]
            return Matrix(temp)
        else:
            raise Exception(f'Shape not compatible for dot product')

    def sum(self):
        return sum([sum(i) for i in self.list])

def randIntMatrix(i, j, s, e):
    temp = [[random.randint(s,e) for _ in range(j)] for _ in range(i)]
    return Matrix(temp)