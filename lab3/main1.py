from math import *


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
    return C, N


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


def learning_cycle():
    new_V = []
    for i in range(len(V)):
        new_V.append(V[i])
    Y = [-1] * 16
    E = 0
    for i in N2:
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


correct_data = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0],
                [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1],
                [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0],
                [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
                [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0],
                [1, 1, 1, 1]]
F = [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
C, N = c_count()
N2 = [2, 13, 15]
V = [0] * (len(C) + 1)
error = learning_cycle()
steps = 1
while (error > 0):
    error = learning_cycle()
    steps += 1

print(V, '\n Done in', steps, 'steps')
