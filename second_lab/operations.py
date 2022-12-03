from math import *
import random
import copy

def transposeMatrix(matrix):
    matrix = copy.deepcopy(matrix)
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    #транспонирование матрицы

def multiMatrix(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    zip_b = zip(*b)
    zip_b = list(zip_b)  # массив столбцов второй матрицы   
    
    # zip(row_a, col_b) - массив из пар элемента строки первой матрицы и элемента столбца второй матрицы
    # перемножаем эту пару, складываем

    return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b] for row_a in a]

def sumMatrix(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    # сумма матриц А и В

def diffMatrix(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    #разность матриц А и В

def genInputMatrix(seq, p, L):
    #генерация входной матрицы
    return [[seq[i+l] for i in range(p)] for l in range(L)]
    
def genWeightMatrix(p, L):
    # матрица весов 1-го слоя
    firstWeightMatrix = [[random.uniform(-0.1, 0.1) for j in range(L)] for i in range(p+1)]
    # матрица весов 2-го слоя
    secondWeightMatrix = [[random.uniform(-0.1, 0.1) for j in range(1)] for i in range(L)]

    return firstWeightMatrix, secondWeightMatrix#, contextWeightMatrix

def vectorModule(w_vector):
    # модель вектора
    w_vector = copy.deepcopy(w_vector)
    return sqrt(sum([i ** 2 for i in w_vector]))

def saveWeightMatrix(firstWeightMatrix, secondWeightMatrix, contextMatrix):
    # сохранение весов
    with open('matrix_1.txt', 'w') as f:
        for i in range(len(firstWeightMatrix)):
            for j in range(len(firstWeightMatrix[0])):
                f.write(f"{firstWeightMatrix[i][j]} ")
            f.write('\n')

    with open('matrix_2.txt', 'w') as f:
        for i in range(len(secondWeightMatrix)):
            for j in range(len(secondWeightMatrix[0])):
                f.write(f"{secondWeightMatrix[i][j]} ")
            f.write('\n')

    with open('context.txt', 'w') as f:
        for i in range(len(contextMatrix)):
            for j in range(len(contextMatrix[0])):
                f.write(f"{contextMatrix[i][j]} ")
            f.write('\n')

def pickOneMatrix(file):
    # получить сохраненные веса одной матрицы
    with open(file, 'r') as file:
        matrix = file.readlines()

    return [[float(n) for n in x.split()] for x in matrix]

def pickWeightMatrix():
    # получить сохраненные веса всех матриц
    return pickOneMatrix('matrix_1.txt'), pickOneMatrix('matrix_2.txt'), pickOneMatrix('context.txt')[0]
