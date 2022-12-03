from tqdm import tqdm
from functions import *
from operations import *
import copy

def predictStep(i, inputMatrix, contextMatrix, firstWeightMatrix, secondWeightMatrix):
    input = inputMatrix[i] + contextMatrix
    S = multiMatrix([input], firstWeightMatrix)
   
    Y = multiMatrix(S, secondWeightMatrix)

    return Y


def predict():
    firstWeightMatrix, secondWeightMatrix, contextMatrix = pickWeightMatrix()
    p = len(firstWeightMatrix) -1
    L = len(firstWeightMatrix[0])

    action = float(input('Choose ur seq:\n1. ArithSeq\n2. DegreeSeq\n3. PeriodSeq\n4. FibSeq\n'))
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
        
    inputMatrix = genInputMatrix(seq, p, L+1)
    
    
    
   
    for i in range(len(inputMatrix) - 1):
        output = predictStep(i, inputMatrix, contextMatrix, firstWeightMatrix, secondWeightMatrix)
        
        print(inputMatrix[i], output[0][0])

