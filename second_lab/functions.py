import math

def degreeFill(z, n):
    matrix = []
    for i in range(0,n):
        matrix.append(z**i)

    return matrix

def periodFill(n):
    matrix = []
    for i in range(0, n):
        if n % 2 == 0 and n % 4 != 0:
            matrix.append(1)
        elif n % 4 == 0:
            matrix.append(-1)
        else:
            matrix.append(0)

    return matrix

def arithFill(z, n, p):
    matrix = []
    for i in range(0, n):
        matrix.append(z+ i*p)

    return matrix

def fibFill(n):
    matrix = []
    for i in range(0, n):
        matrix.append(fibRecursion(i))

    return matrix

def fibRecursion(n):
    if n <= 1:
        return n
    else:
        return fibRecursion(n - 1) + fibRecursion(n - 2)

def initSeq(L):
    action = int(input('Choose ur seq:\n1. ArithSeq\n2. DegreeSeq\n3. PeriodSeq\n4. FibSeq\n'))

    z = int(input('Input z: '))
    if action == 1:
        v = int(input('Input v: '))
        seq = arithFill(z, L*5, v)
    elif action == 2:
        seq = degreeFill(z, L*5)
    elif action == 3:
        seq = periodFill(L*5)
    elif action == 4:
        seq = fibFill(L*3)
    
    return seq

def eluV(vector, alpha):
    for i in range(len(vector)):        
        vector[i] = elu(alpha, vector[i])

    return [vector]

def elu(alpha, i):
    if i < 0:
        return alpha * (math.exp(i) - 1)
    else:
        return i

def deeluV(vector, alpha):
    for i in range(len(vector)):
        if vector[i] <= 0:
            vector[i] = elu(alpha, vector[i]) + alpha
        else:
            vector[i] = 1

    return [vector]
