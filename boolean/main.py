class Perceptron:
    learning_norm = 0.3

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
        return 1 if net >= 0 else 0

    def sigmoid_func(self, net):
        result = 0.5 * (net / (1 + abs(net)) + 1)
        return 1 if result >= 0.5 else 0

    def sigmoid_derivative(self, net):
        return 0.5 / ((abs(net) + 1)**2)

    # mode 's' - sigmoid function
    # other modes - threshold function
    def learning_cycle(self, data, correct_data, mode='s'):
        error_count = 0
        print('Weights: ' + self.weights.__str__() + '\n')
        new_weights = []
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

            new_weights = self.weights
            for i in range(len(self.weights)):
                new_weights[i] += self.learning_norm * (correct_data[cycle] - current_result)\
                                   * derivative(net) * self.values[i]

            if correct_data[cycle] != current_result:
                error_count += 1

        self.weights = new_weights
        return error_count

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

small_table = [
    [0, 0, 1, 0], [0, 1, 0, 1], [0, 1, 1, 0],
    [1, 0, 1, 0], [1, 1, 0, 0],
]

correct = [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
small_correct = [1, 0, 0, 0, 1]

perceptron.set_weights([0, 0, 0, 0, 0])
steps = 0

while perceptron.learning_cycle(table, correct, 's') != 0:
    steps += 1


print('DONE in ' + steps.__str__() + ' steps by threshold function')
print('Weights: ' + perceptron.weights.__str__())
#
# perceptron.set_weights([0, 0, 0, 0, 0])
# steps = 0
#
# while perceptron.learning_cycle(small_table, small_correct, 'o') != 0:
#     steps += 1
# #
# print('\n' + 'DONE in ' + steps.__str__() + ' steps by sigmoid function')
# print('Weights: ' + perceptron.weights.__str__())


err = 0
new_answer = perceptron.get_result(table)
for i in range(len(new_answer)):
    if new_answer[i] != correct[i]:
        err += 1
if err == 0:
    print('\n' + 'CORRECT')


print('\n' + perceptron.get_result(table).__str__())
