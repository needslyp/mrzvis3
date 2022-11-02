import os
import numpy as np
from tqdm import tqdm
from funcs import *


def decompress():
    print('Enter filename(without .npz): ')
    for filename in os.listdir("saved"):
        print('- ', filename)

    filename = input()  # выбор файла

    load = np.load(f'saved/{filename}.npz', allow_pickle=True)

    Y = load['Y_End']

    blockWidth, blockHeight, imgWidth, imgHeight = load['blockParams']

    with open('matrix_2.txt', 'r') as file:
        secondWeightMatrix = file.readlines()
    secondWeightMatrix = [[float(n) for n in x.split()] for x in secondWeightMatrix]

    X_End = []
    for i in tqdm(range(len(Y))):
        X = multiMatrix(Y[i], secondWeightMatrix)
        X_End.append(X)

    X_End = splitToRgbMatrix(X_End)

    resultMatrix = [[0 for j in range(imgHeight)] for i in range(imgWidth)]
    X_End = copy.deepcopy(X_End)

    resultMatrix = toPixels(resultMatrix, X_End, blockWidth, blockHeight)
    drawFromNetwork(resultMatrix, filename, folder='result')