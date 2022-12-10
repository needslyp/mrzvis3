import os
from operations import *
from math import tanh

def chooseFile():
    print('Enter filename: ')
    for filename in os.listdir("images"):
        print(f'- ', filename)

    filename = input()

    new_lst = printToMatrix('images', filename)

    return filename, new_lst
    
def initInput():
    print('choose ur file: ')
    filename, image = chooseFile()
    row, cols = len(image), len(image[0])
    image = [[-1 if x == 0 else x for x in row] for row in image]
    image = [sum(image, [])]

    image = transposeMatrix(image)

    inputMatrix = printToMatrix('input', filename) 
    inputMatrix = [sum([[-1 if x == 0 else x for x in row] for row in inputMatrix], [])]
    inputMatrix = transposeMatrix(inputMatrix)
    return filename, image, row, cols, inputMatrix

def makeCheck(outputMatrix, inputMatrix):
    countNeuro = 0
    for i in range(len(outputMatrix)):
        for j in range(len(outputMatrix[0])):
            outputMatrix[i][j] = tanh(outputMatrix[i][j])

        if outputMatrix[i][0] == inputMatrix[i][0]:
            countNeuro += 1
    return countNeuro

def makeWeight():
    weights = int(input('Took weights: '))
    images = []
    for i in range(weights):
        filename, image = chooseFile()
        
        image = [sum([[-1 if x == 0 else x for x in row] for row in image], [])]

        image = transposeMatrix(image)
        images.append(image)

    weightMatrix = multiMatrix(images[0], transposeMatrix(images[0]))
    for i in range(1, len(images)):
        weightMatrix1 = multiMatrix(images[i], transposeMatrix(images[i]))
        weightMatrix = sumMatrix(weightMatrix, weightMatrix1)
        
    weightMatrix = make0Diagonal(weightMatrix)
    return weightMatrix

def returnImage(outputMatrix, row, cols):
    outputMatrix = [[0 if round(x) == -1 else x for x in row] for row in outputMatrix]
    outputMatrix = [[1 if round(x) == 1 else x for x in row] for row in outputMatrix]
    outputMatrix = transposeMatrix(outputMatrix)
    outputMatrix = sum(outputMatrix,[])
    returnMatrix = []
    count = 0
    for _ in range(row):
        vector = []
        for j in range(cols):
            vector.append(outputMatrix[count+j])
        count += cols
        returnMatrix.append(vector)
    return returnMatrix

def writeToFile(matrix, folder, filename):
    with open(f'{folder}/{filename}', 'w') as f:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                f.write(f"{matrix[i][j]}")
            f.write('\n')
