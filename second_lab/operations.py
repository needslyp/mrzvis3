from math import *
import random
import copy

def transposeMatrix(mat):
    mat = copy.deepcopy(mat)
    matrix = []
    for i in range(len(mat[0])):
        matrix.append(list())
        for j in range(len(mat)):
            matrix[i].append(mat[j][i])
    return matrix

def multiMatrix(a, b):
    m = len(a)  # a: m × n
    n = len(b)  # b: n × k
    k = len(b[0])

    c = [[None for __ in range(k)] for __ in range(m)]  # c: m × k

    for i in range(m):
        for j in range(k):
            c[i][j] = sum(a[i][kk] * b[kk][j] for kk in range(n))

    return c

def multiMatrixNumber(matrix, numb):
    matrix = copy.deepcopy(matrix)
    res_matrix = []
    for i in range(len(matrix)):
        res_matrix_row = []
        for j in range(len(matrix[0])):
            res_matrix_row.append(numb * matrix[i][j])
        res_matrix.append(res_matrix_row)
    
    return res_matrix

def sumMatrix(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    return [list(map(sum, zip(*i))) for i in zip(a, b)]


def diffMatrix(a, b):
    b = copy.deepcopy(b)
    b = [[-1*i for i in b[l]] for l in range(len(b))]

    return sumMatrix(a,b)

def genInputMatrix(seq, p, L):
    matrix = []
    for l in range(L):
        matrix_row = []
        for i in range(p):
            matrix_row.append(seq[i+l])
        matrix.append(matrix_row)

    return matrix


def genWeightMatrix(p, L):
    firstWeightMatrix = []
    for _ in range(p+1):
        matrix_row = []
        for __ in range(L):
            matrix_row.append(random.uniform(-0.1, 0.1))
        firstWeightMatrix.append(matrix_row)
 
    secondWeightMatrix = []
    for _ in range(L):
        matrix_row = []
        for __ in range(1):
            matrix_row.append(random.uniform(-0.1, 0.1))
        secondWeightMatrix.append(matrix_row)    

    return firstWeightMatrix, secondWeightMatrix

def saveWeightMatrix(files=[]):
    file_number = 1
    for filename in files:
        with open(f'{file_number}.txt', 'w') as f:
            for i in range(len(filename)):
                for j in range(len(filename[0])):
                    f.write(f"{filename[i][j]} ")
                f.write('\n')
        file_number+=1


def pickOneMatrix(file):
    with open(file, 'r') as file:
        matrix = file.readlines()
    
    res_matrix = []
    for x in matrix:
        res_matrix_row = []
        for n in x.split():
            res_matrix_row.append(float(n))
        res_matrix.append(res_matrix_row)

    return res_matrix


def pickWeightMatrix():
    return pickOneMatrix('1.txt'), pickOneMatrix('2.txt'), pickOneMatrix('3.txt')[0]
