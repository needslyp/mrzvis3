from PIL import Image, ImageDraw
from math import sqrt
import random
import copy


def getImage(filename):
    image = Image.open('img/' + filename)  # открываем изображение
    imgWidth = image.size[0]  # определяем ширину
    imgHeight = image.size[1]  # определяем высоту
    pixMatrix = image.load()  # выгружаем значения пикселей
    print('Filename size: ', imgWidth, 'x', imgHeight)

    return imgWidth, imgHeight, pixMatrix

def inputBlocks(imgWidth, imgHeight):
    print('Please, enter size of blocks: ')
    blockWidth = int(input('width: '))
    if blockWidth > imgWidth:
        print('Too much value. Please, try again')
        blockWidth = int(input('width: '))

    blockHeight = int(input('height: '))
    if blockHeight > imgHeight:
        print('Too much value. Please, try again')
        blockHeight = int(input('height: '))

    return blockWidth, blockHeight

def transposeMatrix(matrix):
    matrix = copy.deepcopy(matrix)
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    #транспонирование матрицы

def multiMatrix(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    zip_b = zip(*b)
    zip_b = list(zip_b)  # массив столбцов второй матрицы

    return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b] for row_a in a]

    # zip(row_a, col_b) - массив из пар элемента строки первой матрицы и элемента столбца второй матрицы
    # перемножаем эту пару, складываем

def sumMatrix(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    # сумма матриц А и В

def devMatrix(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    #разность матриц А и В

def genColorMatrix(imgWidth, imgHeight, pixMatrix):
    rgbMatrix = []

    # перевод пикселей в шкалу от -1 до 1
    for x in range(imgWidth):
        rgbRow = []
        for y in range(imgHeight):
            r = pixMatrix[x, y][0]
            g = pixMatrix[x, y][1]
            b = pixMatrix[x, y][2]

            rgbPix = [(2 * r / 255) - 1, (2 * g / 255) - 1, (2 * b / 255) - 1]
            rgbRow.append(rgbPix)

        rgbMatrix.append(rgbRow)

    return rgbMatrix

def mirror(rgbMatrix, blockWidth, blockHeight):
    blocks = []
    mirror_iter = 1

    # разбиение на блоки с отзеркаливанием
    if len(rgbMatrix) % blockWidth != 0:
        while len(rgbMatrix) % blockWidth != 0:
            rgbMatrix.append(rgbMatrix[-mirror_iter])
            mirror_iter += 1

    if len(rgbMatrix[0]) % blockHeight != 0:
        while len(rgbMatrix[0]) % blockHeight != 0:
            if len(rgbMatrix[0]) % blockHeight == 0:
                break
            for item in range(len(rgbMatrix)):
                rgbMatrix[item].append(rgbMatrix[item][-1])

    for i in range(0, len(rgbMatrix), blockWidth):
        for j in range(0, len(rgbMatrix[0]), blockHeight):
            line = []
            for x in range(blockWidth):
                for y in range(blockHeight):
                    line += rgbMatrix[i + x][j + y]
            blocks.append(line)
    return blocks

def drawFromNetwork(rgbMatrix, filename, folder=''):
    imgWidth = len(rgbMatrix)
    imgHeight = len(rgbMatrix[0])
    image = Image.new('RGB', (imgWidth, imgHeight), 'white')
    draw = ImageDraw.Draw(image)
    for x in range(imgWidth):
        for y in range(imgHeight):
            draw.point((x, y), (int(255 * (rgbMatrix[x][y][0] + 1) / 2), int(255 * (rgbMatrix[x][y][1] + 1) / 2),
                                int(255 * (rgbMatrix[x][y][2] + 1) / 2)))
    image.save(f'{folder}/' + filename, "JPEG")
    #перевод из нейронов в картинку и отрисовка ее в файл

def toPixels(resultMatrix, X, blockWidth, blockHeight):
    n=0
    for i in range(0, len(resultMatrix), blockWidth):
        for j in range(0, len(resultMatrix[0]), blockHeight):
            m = 0
            for x in range(blockWidth):
                for y in range(blockHeight):
                    resultMatrix[i + x][j + y] = []
                    resultMatrix[i + x][j + y] += X[n][m]
                    m += 1
            n += 1
    return resultMatrix
    #перевод пикселей из блоков обратно в картинку

def genWeightMatrix(firstLayerNeuron, blocks):
    # матрица весов 1-го слоя
    firstWeightMatrix = [[random.uniform(-0.1, 0.1) for j in range(firstLayerNeuron)] for i in range(len(blocks[0]))]
    # матрица весов 2-го слоя
    secondWeightMatrix = transposeMatrix(firstWeightMatrix)

    return firstWeightMatrix, secondWeightMatrix

def alpha(matrix):
    matrix = copy.deepcopy(matrix)
    return 1 / multiMatrix(matrix, transposeMatrix(matrix))[0][0]
    #адаптивный шаг

def vectorModule(w_vector):
    w_vector = copy.deepcopy(w_vector)
    return sqrt(sum([i ** 2 for i in w_vector]))

def correctWeightMatrix(firstWeightMatrix, secondWeightMatrix, Y, dX, X=[], layer=1):
    firstWeightMatrix = copy.deepcopy(firstWeightMatrix)
    secondWeightMatrix = copy.deepcopy(secondWeightMatrix)
    Y = copy.deepcopy(Y)
    X = copy.deepcopy(X)
    dX = copy.deepcopy(dX)

    if layer == 1:
        alphaX = alpha(X)
        saveMatrix = multiMatrix(transposeMatrix(X), dX)
        saveMatrix = multiMatrix(saveMatrix, transposeMatrix(secondWeightMatrix))
        saveMatrix = [[alphaX * saveMatrix[i][j] for j in range(len(saveMatrix[0]))] for i in range(len(saveMatrix))]

        return devMatrix(firstWeightMatrix, saveMatrix)

    else:
        alphaY = alpha(Y)
        saveMatrix = multiMatrix(transposeMatrix(Y), dX)
        saveMatrix = [[alphaY * saveMatrix[i][j] for j in range(len(saveMatrix[0]))] for i in range(len(saveMatrix))]

        return devMatrix(secondWeightMatrix, saveMatrix)

def normalWeightMatrix(weightMatrix):
    weightMatrix = copy.deepcopy(weightMatrix)
    return [[weightMatrix[i][j] / vectorModule(weightMatrix[i]) for j in range(len(weightMatrix[0]))] for i in range(len(weightMatrix))]
    #нормирование матрицы

def sqrtError(dX):
    dX = copy.deepcopy(dX)
    dx_sqrt_list = list(map(lambda x: x ** 2, dX[0]))
    return sum(dx_sqrt_list)
    #подсчет квадратичной ошибки

def trainStep(i, blocks, firstWeightMatrix, secondWeightMatrix):
    Y = multiMatrix([blocks[i]], firstWeightMatrix)
    X = multiMatrix(Y, secondWeightMatrix)
    dX = devMatrix(X, [blocks[i]])

    # обучение
    saveMatrix = secondWeightMatrix
    secondWeightMatrix = correctWeightMatrix(firstWeightMatrix, secondWeightMatrix, Y, dX, layer=2)
    firstWeightMatrix = correctWeightMatrix(firstWeightMatrix, saveMatrix, Y, dX, X=X)
    #firstWeightMatrix = normalWeightMatrix(firstWeightMatrix)
    #secondWeightMatrix = normalWeightMatrix(secondWeightMatrix)

    return firstWeightMatrix, secondWeightMatrix, dX

def splitToRgbMatrix(X_End):
    for i in range(len(X_End)):
        X_End[i] = X_End[i][0]

    for i in range(len(X_End)):
        X_End[i] = [X_End[i][j:j + 3] for j in range(0, len(X_End[i]), 3)]

    return X_End

def compressionRatio(N, L, p):
    return (N*L)/((N+L)*p+2)

def saveWeightMatrix(firstWeightMatrix, secondWeightMatrix):
    # сохранение весов
    with open('matrix_1.txt', 'w') as f:
        for i in range(len(firstWeightMatrix)):
            for j in range(len(firstWeightMatrix[0])):
                f.write(f"{firstWeightMatrix[i][j]} ")
            f.write('\n')

    with open('matrix_2.txt', 'w') as f:
        for i in range(len(secondWeightMatrix)):
            for j in range(len(secondWeightMatrix[0])):
                f.write(f"{secondWeightMatrix[i][j]} ")
            f.write('\n')