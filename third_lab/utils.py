import os
from operations import *
from math import tanh

def chooseFile():
    filename = input()

    new_lst = makeMatrix(f'images/{filename}')

    return filename, new_lst
    
def initInput():
    print('choose ur file: ')
    filename, st_image = chooseFile()

    image = transposeMatrix([fromMatrixTo1Line(st_image)])

    return filename, len(st_image), len(st_image[0]), image

def makeCheck(outputMatrix, inputMatrix):
    counter = 0
    for i in range(len(outputMatrix)):
        outputMatrix[i][0] = tanh(outputMatrix[i][0])

        if outputMatrix[i][0] == inputMatrix[i][0]:
            counter += 1

    return counter

def makeWeight():
    weights = int(input('Took weights: '))
    images = []
    for i in range(weights):
        filename, image = chooseFile()
        
        image = transposeMatrix([fromMatrixTo1Line(image)])
        images.append(image)

    weightMatrix = multiMatrix(images[0], transposeMatrix(images[0]))
    for i in range(1, len(images)):
        weightMatrix = sumMatrix(weightMatrix, multiMatrix(images[i], transposeMatrix(images[i])))

    for i in range(len(weightMatrix)):
        for j in range(len(weightMatrix[0])):
            if i == j:
                weightMatrix[i][j] = 0

    return weightMatrix

def returnImage(outputMatrix, row, cols):
    outputMatrix = roundMatrix(outputMatrix)
    returnMatrix = []
    count = 0
    for _ in range(row):
        vector = []
        for j in range(cols):
            vector.append(outputMatrix[count+j])
        count += cols
        returnMatrix.append(vector)

    return returnMatrix

def writeToFile(returnMatrix, path):
    with open(path, 'w') as f:
        for i in range(len(returnMatrix)):
            for j in range(len(returnMatrix[0])):
                f.write(f"{returnMatrix[i][j]}")
            f.write('\n')
