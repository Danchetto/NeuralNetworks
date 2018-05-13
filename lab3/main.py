import math

class Perceptron:
    learning_norm = 0.3

    def set_values(self, data_x):
        self.values = [1]
        self.values.extend(data_x)

    def set_weights(self, data_w):
        self.weights = data_w.copy()

    def Fj(self, x, c, j):
        result = 0
        for i in range(4):
            result += x[i] + c[j][i]
        return math.exp(-(result ** 2))

    def net_count(self, c, n):
        result = 0
        for i in range(len(self.values)):
            result += self.weights[i] * self.Fj(self.values, c, n)

        return result

    def activation_func(self, net):
        return 1 if net >= 0 else 0


    # mode 's' - sigmoid function
    # other modes - threshold function
    def learning_cycle(self, data, correct_data, c, mode='s'):
        error_count = 0
        print('Weights: ' + self.weights.__str__() + '\n')
        new_weights = self.weights.copy()

        for n in range(5):
            for cycle in range(len(data)):
                self.set_values(data[cycle])
                net = self.net_count(c, n)
                current_result = self.activation_func(net)

                for i in range(len(self.weights)):
                    new_weights[i] += self.learning_norm * (correct_data[cycle] - current_result)\
                                       * self.Fj(self.values,c,n)

                if correct_data[cycle] != current_result:
                    error_count += 1

        self.set_weights(new_weights)
        return error_count

    # def get_result(self, table):
    #     result = []
    #     for data in table:
    #         self.set_values(data)
    #         result.append(self.sigmoid_func(self.net_count()))
    #
    #     return result

perceptron = Perceptron()

table = [
    [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1],
    [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1],
    [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
    [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1],
]

#min data for learning
small_table = [
    [0, 0, 1, 0], [0, 1, 0, 1], [0, 1, 1, 0],
    [1, 0, 1, 0], [1, 1, 0, 0],
]

correct = [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
small_correct = [1, 0, 0, 0, 1]
C = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]]

perceptron.set_weights([0, 0, 0, 0, 0])
steps = 0
errors = [perceptron.learning_cycle(table, correct, 't')]
while errors[-1] != 0:
    errors.append(perceptron.learning_cycle(table, correct, 't'))
    steps += 1

print('DONE in ' + steps.__str__() + ' steps by threshold function')
print('Weights: ' + perceptron.weights.__str__() + '\n')

