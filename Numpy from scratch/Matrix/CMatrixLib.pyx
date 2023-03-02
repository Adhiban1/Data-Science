def matrixAdd(list a, list b, int rows, int columns):
    return [[a[i][j] + b[i][j] for j in range(columns)] for i in range(rows)]

def matrixSub(list a, list b, int rows, int columns):
    return [[a[i][j] - b[i][j] for j in range(columns)] for i in range(rows)]

def matrixMul(list a, list b, int rows, int columns):
    return [[a[i][j] * b[i][j] for j in range(columns)] for i in range(rows)]

def matrixDiv(list a, list b, int rows, int columns):
    return [[a[i][j] / b[i][j] for j in range(columns)] for i in range(rows)]

def matrixFloorDiv(list a, list b, int rows, int columns):
    return [[a[i][j] / b[i][j] for j in range(columns)] for i in range(rows)]

def dot(list a, list b, int l, int m, int n):
    temp = [[0 for _ in range(n)] for _ in range(l)]
    for i in range(l):
        for k in range(n):
            for j in range(m):
                temp[i][k] += a[i][j] * b[j][k]
    return temp


def matrixAdd_s(list a, float b, int rows, int columns):
    return [[a[i][j] + b for j in range(columns)] for i in range(rows)]

def matrixSub_s(list a, float b, int rows, int columns):
    return [[a[i][j] - b for j in range(columns)] for i in range(rows)]

def matrixMul_s(list a, float b, int rows, int columns):
    return [[a[i][j] * b for j in range(columns)] for i in range(rows)]

def matrixDiv_s(list a, float b, int rows, int columns):
    return [[a[i][j] / b for j in range(columns)] for i in range(rows)]

def matrixFloorDiv_s(list a, float b, int rows, int columns):
    return [[a[i][j] // b for j in range(columns)] for i in range(rows)]