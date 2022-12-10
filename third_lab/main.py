from utils import *


filename, image, row, cols, inputMatrix = initInput()
weightMatrix = makeWeight()


relax = False
iteration = 0

while relax == False:
    outputMatrix = multiMatrix(weightMatrix, inputMatrix)

    countNeuro = makeCheck(outputMatrix, inputMatrix)

    iteration += 1
    print(f'Iteration #{iteration}\n{len(outputMatrix) - countNeuro}')

    if countNeuro == len(outputMatrix):
        relax = True
        print(f'\nRelaxation!!!\nFinal iteration: {iteration}')
        
        returnMatrix = returnImage(outputMatrix, row, cols)

        writeToFile(returnMatrix, 'output', filename)

    else:
        inputMatrix = outputMatrix

