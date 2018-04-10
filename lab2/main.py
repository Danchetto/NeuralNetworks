class Perceptron:
    learning_norm = 0.5
    p = 4

    def set_values(self, data_x):
        self.values = [1]
        self.values.extend(data_x)

    def set_weights(self, data_w):
        self.weights = data_w

    def next_x(self):
        result = 0
        for i in range(len(self.values)):
            result += self.values[i] * self.weights[i]
        return result

    def learning_cycle(self, correct_data):
        error_count = 0
        print('Weights: ' + self.weights.__str__() + '\n')
        counter = self.p
        new_weights = []
        while counter < 20:
            values = []
            for cycle in range(self.p):
                values.append(correct_data[counter - self.p - cycle + 1])

            self.set_values(values)
            current_result = round(self.next_x(), 6)
            print(current_result)

            new_weights = self.weights
            for i in range(len(self.weights)):
                new_weights[i] += self.learning_norm * (correct_data[counter] - current_result) * self.values[i]

            if correct_data[counter] != current_result:
                error_count += 1

            counter += 1
        self.weights = new_weights
        return error_count

    # def get_result(self, a):
    #     result = []
    #     for data in table:
    #         self.set_values(data)
    #         result.append(self.next_x())
    #
    #     return result


perceptron = Perceptron()

correct_data = []
a = -1
b = 1
delta = abs(a - b) / 20
def my_func(x):
    return x**2

for i in range(1, 22):
    correct_data.append(round(my_func(a), 6))
    a += delta

perceptron.set_weights([0, 0, 0, 0, 0])

steps = 0
while perceptron.learning_cycle(correct_data) != 0:
    steps += 1
    continue

print("DONE in {steps} steps".format(steps=steps))
