import math
import matplotlib.pyplot as plt

class Perceptron:
    learning_norm = 0.5
    p = 4
    values = []

    def set_values(self, data_x):
        self.values = [1]
        self.values.extend(data_x)

    def set_weights(self, data_w):
        self.weights = data_w.copy()

    def next_x(self):
        result = 0
        for i in range(len(self.values)):
            result += self.values[i] * self.weights[i]
        return result

    def learning_cycle(self, learning_data, correct_data):
        print('Weights: ' + self.weights.__str__() + '\n')
        print('Values: ' + self.values.__str__() + '\n')
        counter = self.p
        new_weights = self.weights.copy()
        all_result = correct_data[0:self.p].copy()
        while counter <= 20:
            values = []
            for cycle in range(self.p):
                values.append(correct_data[counter - self.p + cycle])

            self.set_values(values)
            current_result = self.next_x()
            all_result.append(current_result)

            for i in range(len(self.weights)):
                new_weights[i] += self.learning_norm * (correct_data[counter] - current_result) * self.values[i]

            counter += 1

        self.set_weights(new_weights)
        return all_result


def error_function(x, correct_x):
    diff = []
    for i in range(len(x)):
        diff.append((x[i] - correct_x[i]) ** 2)
    return math.sqrt(sum(diff))


perceptron = Perceptron()

correct_data = []
x = []
left = -1
right = 1
delta = abs(left - right) / 20


def square(x):
    return x**2


for i in range(1, 22):
    correct_data.append(round(square(left), 6))
    x.append(left)
    left += delta

learning_data = correct_data.copy()

perceptron.set_weights([0, 0, 0, 0, 0])

steps = 0
while steps < 100:
    learning_data = perceptron.learning_cycle(learning_data, correct_data)
    steps += 1
    continue

result = perceptron.learning_cycle(learning_data, correct_data)
error = round(error_function(result, correct_data), 5)
print(result)
print(correct_data)
print('Error = ', error)

print("DONE in {steps} steps".format(steps=steps))
