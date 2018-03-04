import math

class Perceptron:
    learning_norm = 0.2

    def set_values(self, data_x):
        self.values = [1]
        self.values.extend(data_x)

    def set_weights(self, data_w):
        self.weights = data_w

    def net_count(self):
        result = 0
        for i in range(len(self.values)):
            result += self.values[i] * self.weights[i]

        return result

    def threshold_func(self, net):
        if net >= 0:
            return 1
        else:
            return 0

    def sigmoid_func(self, net):
        result = 0.5 * (net / (1 + abs(net)) + 1)
        if result >= 0.5:
            return 1
        else:
            return 0

    def sigmoid_derivative(self, net):
        return 0.5 / ((abs(net) + 1)**2)

    # mode 's' - sigmoid function
    # other - threshold function
    def learning_cycle(self, data, correct_data, mode='s'):
        E = 0

        if mode == 's':
            derivative = self.sigmoid_derivative
            activate_function = self.sigmoid_func
        else:
            derivative = lambda x: 1
            activate_function = self.threshold_func

        for cycle in range(len(data)):
            self.set_values(data[cycle])
            net = self.net_count()
            current_result = activate_function(net)

            for i in range(len(self.weights)):
                self.weights[i] += self.learning_norm * (correct_data[cycle] - current_result)\
                                   * derivative(net) * self.values[i]

            if correct_data[cycle] != current_result:
                E += 1
        # print(current_result)
        return E

    def get_result(self, table):
        result = []
        for data in table:
            self.set_values(data)
            result.append(self.sigmoid_func(self.net_count()))

        return result


perceptron = Perceptron()

table = [
    [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1],
    [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1],
    [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
    [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1],
]

correct = [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]

perceptron.set_weights([0, 0, 0, 0, 0])

steps = 0

while perceptron.learning_cycle(table, correct, 'o') != 0:
    steps += 1


print('DONE in ' + steps.__str__() + ' steps by threshold function')
print('Weights: ' + perceptron.weights.__str__())

perceptron.set_weights([0, 0, 0, 0, 0])

steps = 0

while perceptron.learning_cycle(table, correct) != 0:
    steps += 1

print('DONE in ' + steps.__str__() + ' steps by sigmoid function')
print('Weights: ' + perceptron.weights.__str__())

print(perceptron.get_result(table))
