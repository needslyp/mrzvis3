from functions import *
from operations import *


def predictStep(i, inputMatrix, contextMatrix, firstWeightMatrix, secondWeightMatrix):
    S = multiMatrix([inputMatrix[i] + contextMatrix], firstWeightMatrix)
    print(inputMatrix[i], multiMatrix(S, secondWeightMatrix)[0][0])


def predict():
    firstWeightMatrix, secondWeightMatrix, contextMatrix = pickWeightMatrix()

    seq = initSeq(len(firstWeightMatrix[0]))
        
    inputMatrix = genInputMatrix(seq, len(firstWeightMatrix) - 1, len(firstWeightMatrix[0]) + 1)
    
    for i in range(len(inputMatrix) - 1):
        predictStep(i, inputMatrix, contextMatrix, firstWeightMatrix, secondWeightMatrix)
