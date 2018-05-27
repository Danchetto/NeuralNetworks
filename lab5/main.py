import numpy as np


class HopfieldNetwork:
    def __init__(self):
        self.F = [[1, 1, 1, 1, 1,
                  1, -1, 1, -1, -1,
                  1, -1, 1, -1, -1,
                  1, -1, 1, -1, -1]]
        self.H = [[1, 1, 1, 1, 1,
                  -1, -1, 1, -1, -1,
                  -1, -1, 1, -1, -1,
                  1, 1, 1, 1, 1]]
        self.J = [[1, -1, -1, 1, -1, 1, -1, -1, -1, 1,
                  1, -1, -1, -1, 1,
                  1, 1, 1, 1, -1]]

        self.W = np.dot(np.array(self.F).transpose(), np.array(self.F)) + \
                 np.dot(np.array(self.H).transpose(), np.array(self.H)) + \
                 np.dot(np.array(self.J).transpose(), np.array(self.J))

        for i in range(len(self.W[0])):
            self.W[i][i] = 0

        self.prevY = self.Y = []

    def net_count(self):
        result = []
        for i in range(len(self.prevY)):
            result.append(sum([self.W[j][i] * self.prevY[j] for j in range(len(self.prevY))]))
        return result

    def out_function(self, net):
        out = []
        for i in range(len(self.prevY)):
            if net[i] > 0:
                cur = 1
            elif net[i] < 0:
                cur = -1
            else:
                cur = self.prevY[i]
            out.append(cur)
        self.prevY = out.copy()
        return out

    def get_result(self, data):
        self.prevY = data
        net = self.net_count()
        result = self.out_function(net)
        if result == self.F[0]:
            return 'F'
        elif result == self.H[0]:
            return 'H'
        elif result == self.J[0]:
            return 'J'
        return 'error'


network = HopfieldNetwork()
test = [-1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1]
print(test)
print(network.get_result(test))
