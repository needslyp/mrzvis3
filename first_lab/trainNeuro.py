import os
from tqdm import tqdm
from funcs import *


def trainNeuro():
    # считывание файлов
    print('Enter filename: ')
    for filename in os.listdir("img"):
        print('- ', filename)
    filename = input()

    imgWidth, imgHeight, pixMatrix = getImage(filename)
    rgbMatrix = genColorMatrix(imgWidth, imgHeight, pixMatrix)
    # ввод размера блоков
    blockWidth, blockHeight = inputBlocks(imgWidth, imgHeight)
    blocks = mirror(rgbMatrix, blockWidth, blockHeight)
    print(len(blocks),len(blocks[0]), len(blocks[0]))

    # ввести количество нейронов на скрытом слое
    print(f'In your block there are {len(blocks[0])} input neurons.')
    firstLayerNeuron = int(input('Enter count of neurons in the first layer: '))

    e = float(input('Input square error: '))
    firstWeightMatrix, secondWeightMatrix = genWeightMatrix(firstLayerNeuron, blocks)
    iteration = 1

    # нейросеть
    while True:
        sumErr = 0
        for i in tqdm(range(len(blocks))):
            firstWeightMatrix, secondWeightMatrix, dX = trainStep(i, blocks, firstWeightMatrix,secondWeightMatrix)
            sumErr += sqrtError(dX)
        print(f'\nError {iteration}: ', sumErr)
        iteration += 1

        # запись результата
        if sumErr < e:
            print('Compression ratio: ', compressionRatio(len(blocks[0]), iteration, firstLayerNeuron))
            saveWeightMatrix(firstWeightMatrix, secondWeightMatrix)
            break