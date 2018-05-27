from math import *
from pylab import *
from matplotlib import mlab


def c_count():
    C = []
    N = []
    kol = 0
    for i in F:
        if (i == 1):
            kol += 1
    if (kol <= 8):
        m = 1
    else:
        m = 0
    for i in range(16):
        if (F[i] == m):
            N.append(i)
            C.append(correct_data[i][:])
    return C


def Fe(i, data):
    summ = 0
    for j in range(4):
        summ += (data[j] - C[i][j]) * (data[j] - C[i][j])
    return exp(-summ)


def net(weights, mat):
    net = 0
    for i in range(len(weights) - 1):
        net += weights[i] * Fe(i, mat)
    net += weights[len(weights) - 1]
    return net


def learning_cycle(V, N):
    new_V = []
    for i in range(len(V)):
        new_V.append(V[i])
    Y = [-1] * 16
    E = 0
    for i in N:
        if (net(V, correct_data[i]) >= 0):
            Y[i] = 1
        else:
            Y[i] = 0
        if (Y[i] != F[i]):
            E += 1
            for j in range(len(V) - 1):
                new_V[j] += - 0.3 * (Y[i] - F[i]) * Fe(j, correct_data[i])
            new_V[len(V) - 1] += - 0.3 * (Y[i] - F[i])
    if (E > 0):
        for i in range(len(V)):
            V[i] = new_V[i]
    return E

def test(V, sett):
    Y = []
    for i in range(16):
        if (net(V, sett[i]) >= 0):
            Y.append(1)
        else:
            Y.append(0)
    return Y

# Меняем минимальные наборы
def Shift(N, P, k):
    if (len(N) == k):
        for i in range(len(N)):
            N[i] = i
        N.append(N[len(N) - 1] + 1)

    else:
        if (N[len(N) - k - 1] == P):
            Shift(N, P - 1, k + 1)
        else:
            N[len(N) - 1 - k] += 1
            for i in range(k + 1):
                N[len(N) - k + i - 1] = N[len(N) - k - 1] + i


def change_vectors(N):
    if (N[len(N) - 1] != 15):
        N[len(N) - 1] += 1
    else:
        Shift(N, 14, 1)

def result_function(N, C):
    k = 1
    while (k != 0):
        V = [0] * (len(C) + 1)
        E = learning_cycle(V, N) # Суммарная ошибка
        kol = 1 # Колличество эпох
        err = []
        err.append(E)
        while (E != 0):
            kol += 1
            E = learning_cycle(V, N)
            err.append(E)
        if (test(V, correct_data) == F):
            k = 0
        else:
            print(N)
            change_vectors(N)
    return V, kol, err


correct_data = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0],
                [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1],
                [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0],
                [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
                [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0],
                [1, 1, 1, 1]]
F = [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
C = c_count()
N = [2, 5, 6, 10, 12]
result = result_function(N, C)
print(result[0])

xlist = mlab.frange(0, result[1] - 1, 1)
plot(xlist, result[2], 'b')
grid(True, linestyle='-', color='0.75')
show()

