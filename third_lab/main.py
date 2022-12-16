from utils import *


filename, rows, cols, inputMatrix = initInput()
weightMatrix = makeWeight()

relax = False
iteration = 0

while relax == False:
    outputMatrix = multiMatrix(weightMatrix, inputMatrix)

    countNeuro = makeCheck(outputMatrix, inputMatrix)

    iteration += 1
    print(f'Iteration #{iteration}\nError: {len(outputMatrix) - countNeuro}')

    if countNeuro != len(outputMatrix):
        inputMatrix = outputMatrix

    else:
        relax = True
        print(f'\nRelax!!!\n')
        
        returnMatrix = returnImage(outputMatrix, rows, cols)

        writeToFile(returnMatrix, f'output/{filename}')

