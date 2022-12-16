import copy

def makeMatrix(path):
    with open(path, 'r') as file:
        lst = file.readlines()
    
    matrix = []
    for x in lst:
        matrix_row = []
        for n in x[:-1]:
            matrix_row.append(int(n))
        matrix.append(matrix_row)

    return matrix

def fromMatrixTo1Line(matrix):
    returnMatrix = []
    for row in matrix:
        for x in row:
            if x == 0:
                returnMatrix.append(-1)
            else:
                returnMatrix.append(x)

    return returnMatrix

def transposeMatrix(mat):
    mat = copy.deepcopy(mat)
    matrix = []
    for i in range(len(mat[0])):
        matrix.append(list())
        for j in range(len(mat)):
            matrix[i].append(mat[j][i])

    return matrix

def sumMatrix(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)

    return [list(map(sum, zip(*i))) for i in zip(a, b)]

def multiMatrix(a, b):
    m = len(a)  # a: m × n
    n = len(b)  # b: n × k
    k = len(b[0])

    c = [[None for __ in range(k)] for __ in range(m)]  # c: m × k

    for i in range(m):
        for j in range(k):
            c[i][j] = sum(a[i][kk] * b[kk][j] for kk in range(n))

    return c

def roundMatrix(outputMatrix):
    result = []
    for row in outputMatrix:
        res_row = []
        for x in row:
            if round(x) == -1:
                res_row.append(0)
            elif round(x) == 1:
                res_row.append(1)
        result.append(res_row)

    outputMatrix = transposeMatrix(result)[0]
    
    return outputMatrix