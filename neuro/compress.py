import os
import numpy as np
from tqdm import tqdm
from funcs import *

def compress():
    # считывание списка файлов
    print('Enter filename: ')
    for filename in os.listdir("img"):
        print('- ', filename)

    filename = input()  # выбор файла

    imgWidth, imgHeight, pixMatrix = getImage(filename)

    rgbMatrix = genColorMatrix(imgWidth, imgHeight, pixMatrix)

    # ввод размера блоков
    blockWidth, blockHeight = inputBlocks(imgWidth, imgHeight)

    blocks = mirror(rgbMatrix, blockWidth, blockHeight)

    with open('matrix_1.txt', 'r') as file:
        firstWeightMatrix = file.readlines()

    firstWeightMatrix = [[float(n) for n in x.split()] for x in firstWeightMatrix]

    Y_End = []
    for i in tqdm(range(len(blocks))):
        Y = multiMatrix([blocks[i]], firstWeightMatrix)
        Y_End.append(Y)

    blockParams = [blockWidth, blockHeight, imgWidth, imgHeight]

    np.savez_compressed(f'saved/{filename}', blockParams=blockParams, Y_End=Y_End)
