import math

def degreeFill(z, n):
    return [z ** i for i in range(0, n)]

def periodFill(n):
    return [checkPeriod(i) for i in range(n)]

def arithFill(z, n):
    return [z + i for i in range(0, n)]

def fibFill(n):
    return [fibRecursion(i) for i in range(n)]

def checkPeriod(n):
    if n % 2 == 0:
        return 0
    else:
        return 1

def fibRecursion(n):
    if n <= 1:
        return n
    else:
        return fibRecursion(n - 1) + fibRecursion(n - 2)

def eluV(vector, alpha):
    for i in range(len(vector)):        
        vector[i] = elu(alpha, vector[i])

    return vector

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
    return vector
