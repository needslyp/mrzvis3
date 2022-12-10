import copy

def printToMatrix(folder, filename):
    with open(f'{folder}/{filename}', 'r') as file:
        lst = file.readlines()
    new_lst = [[int(n) for n in x[:-1]] for x in lst[:-1]]
    new_lst.append([])
    for i in lst[-1]:
        new_lst[-1].append(int(i))

    return new_lst

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

def make0Diagonal(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = 0

    return matrix