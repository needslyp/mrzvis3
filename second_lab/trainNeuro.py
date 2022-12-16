from functions import *
from operations import *
import copy

def correctWeightMatrix(S, Y, firstWeightMatrix, secondWeightMatrix, inputMatrix, hidden, gamma, alpha, output=[]):
    firstWeightMatrix = copy.deepcopy(firstWeightMatrix)
    secondWeightMatrix = copy.deepcopy(secondWeightMatrix)
    hidden = copy.deepcopy(hidden)
    output = copy.deepcopy(output)
    
        
    interMatrix = multiMatrix(multiMatrix(transposeMatrix([inputMatrix]), transposeMatrix(secondWeightMatrix)), deeluV(S, alpha))
    interMatrix = multiMatrixNumber(interMatrix, alpha*gamma)

    firstWeightMatrix = diffMatrix(firstWeightMatrix, interMatrix)

    interMatrix = multiMatrix(transposeMatrix(hidden), deeluV(Y, alpha))
    interMatrix = multiMatrixNumber(interMatrix, alpha*gamma)

    secondWeightMatrix = diffMatrix(secondWeightMatrix, interMatrix)

    return firstWeightMatrix, secondWeightMatrix

def trainStep(i, inputMatrix, contextMatrix, alpha, firstWeightMatrix, secondWeightMatrix, useNull):
    S = multiMatrix([inputMatrix[i] + contextMatrix], firstWeightMatrix)[0]
    
    hidden = eluV(S, alpha)
    
    Y = multiMatrix(hidden, secondWeightMatrix)[0]
    output = eluV(Y, alpha)
   
    gamma = diffMatrix(output, [[inputMatrix[i+1][-1]]])[0][0]

    firstWeightMatrix, secondWeightMatrix = correctWeightMatrix(S, Y, firstWeightMatrix, secondWeightMatrix, inputMatrix[i] + contextMatrix, hidden, gamma, alpha, output=output)
    
    if useNull:
        contextMatrix = [0]
    else: 
        contextMatrix = output[0]

    return firstWeightMatrix, secondWeightMatrix, contextMatrix, gamma


def trainNeuro():
    p = int(input('Input p: '))
    L = int(input('Input L: '))
    
    alpha = float(input('Input alpha: '))
    e = float(input('Input square error: '))

    seq = initSeq(L)

    useNull = bool(input('Use null context\n0. No\n1. Yes\n')) 

    inputMatrix = genInputMatrix(seq, p, L+1)
    
    firstWeightMatrix, secondWeightMatrix = genWeightMatrix(p, L)
    
    contextMatrix = [0]
    iteration = 1

    while True:
        sumErr = 0
        for i in range(len(inputMatrix)-1):
            firstWeightMatrix, secondWeightMatrix, contextMatrix, gamma = trainStep(i, inputMatrix, contextMatrix, alpha, firstWeightMatrix, secondWeightMatrix, useNull)
            sumErr += (gamma ** 2)

        print('Iter: ', iteration, ' E = ', sumErr)

        iteration += 1

        if sumErr < e or iteration > 10000000: 
            saveWeightMatrix([firstWeightMatrix, secondWeightMatrix, [contextMatrix]])
            break
