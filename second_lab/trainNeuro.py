from functions import *
from operations import *
import copy

def correctWeightMatrix(S, Y, firstWeightMatrix, secondWeightMatrix, inputMatrix, hidden, gamma, alpha, output=[], name=''):
    firstWeightMatrix = copy.deepcopy(firstWeightMatrix)
    secondWeightMatrix = copy.deepcopy(secondWeightMatrix)
    hidden = copy.deepcopy(hidden)
    output = copy.deepcopy(output)
    

    if name == 'first':
        
        saveMatrix = multiMatrix(transposeMatrix([inputMatrix]), transposeMatrix(secondWeightMatrix))
        saveMatrix = multiMatrix(saveMatrix, [deeluV(S[0], alpha)])
        saveMatrix = [[alpha * gamma * saveMatrix[i][j] for j in range(len(saveMatrix[0]))] for i in range(len(saveMatrix))]
    
        return diffMatrix(firstWeightMatrix, saveMatrix)

    elif name == 'second':
        
        saveMatrix = multiMatrix(transposeMatrix(hidden), [deeluV(Y[0], alpha)])
        saveMatrix = [[alpha * gamma * saveMatrix[i][j] for j in range(len(saveMatrix[0]))] for i in range(len(saveMatrix))]

        return diffMatrix(secondWeightMatrix, saveMatrix)

def trainStep(i, inputMatrix, contextMatrix, alpha, firstWeightMatrix, secondWeightMatrix, useNull):
    input = inputMatrix[i] + contextMatrix
    S = multiMatrix([input], firstWeightMatrix)
    
    hidden = [eluV(S[0], alpha)]
    
    Y = multiMatrix(hidden, secondWeightMatrix)
    output = [eluV(Y[0], alpha)]
   
    gamma = diffMatrix(output, [[inputMatrix[i+1][-1]]])[0][0]
    
    
    # обучение
    saveWeightMatrix = secondWeightMatrix
    secondWeightMatrix = correctWeightMatrix(S, Y, firstWeightMatrix, secondWeightMatrix, input, hidden, gamma, alpha, output=output, name = 'second')
    firstWeightMatrix = correctWeightMatrix(S, Y, firstWeightMatrix, saveWeightMatrix, input, hidden, gamma, alpha, output=output, name = 'first')
    
    if useNull:
        contextMatrix = [0]
    else:
        contextMatrix = output[0]

    return firstWeightMatrix, secondWeightMatrix, contextMatrix, gamma, output



def trainNeuro():
    p = int(input('Input p: '))
    L = int(input('Input L: '))
    
    
    alpha = float(input('Input alpha: '))
    e = float(input('Input square error: '))


    action = int(input('Choose ur seq:\n1. ArithSeq\n2. DegreeSeq\n3. PeriodSeq\n4. FibSeq\n'))

    seq = []
    if action == 1:
        z = int(input('Input z: '))
        seq = arithFill(z, L*5)
    elif action == 2:
        z = float(input('Input z: '))
        seq = degreeFill(z, L*5)
    elif action == 3:
        seq = periodFill(L*5)
    elif action == 4:
        seq = fibFill(L*5)

    useNull = bool(input('Use null context\n0. No\n1. Yes\n')) 

    inputMatrix = genInputMatrix(seq, p, L+1)
    
    firstWeightMatrix, secondWeightMatrix= genWeightMatrix(p, L)
    
    contextMatrix = [0]
    iteration = 1

    # нейросеть
    while True:
        sumErr = 0
        for i in range(len(inputMatrix)-1):
            firstWeightMatrix, secondWeightMatrix, contextMatrix, gamma, output = trainStep(i, inputMatrix, contextMatrix, alpha, firstWeightMatrix, secondWeightMatrix, useNull)
            sumErr += (gamma ** 2)

        print('Iter: ', iteration, ' E = ', sumErr)

        iteration += 1

        # запись результата
        if sumErr < e or iteration > 1000000: 
            saveWeightMatrix(firstWeightMatrix, secondWeightMatrix, [contextMatrix])
            break
