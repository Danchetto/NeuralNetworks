import math


def func(x):
    return math.cos(x)

def error_func(x, c_x):
    diff = []
    for i in range(len(x)):
        diff.append((x[i] - c_x[i]) ** 2)
    return math.sqrt(sum(diff))

class Perceptron:

    def __init__(self):
        self.divide_interval = 20
        self.norm = 0.01
        self.p = 4

    def set_x(self, data_x):
        self.values = [1]
        self.values.extend(data_x)

    def set_w(self, data_w):
        self.weights = data_w

    def next_x(self):
        next_value = 0
        for i in range(len(self.values)):
            next_value += self.values[i] * self.weights[i]
        # next_value += float(sum(self.values) / len(self.values))
        return next_value

    def epoch(self, learning_data):
        errors = 0

        print('Weights: ' + self.weights.__str__() + '\n')

        counter = self.p
        new_w = []
        current = []

        while counter < self.divide_interval:
            values = []
            for cycle in range(self.p):
                values.append(learning_data[counter - self.p - cycle + 1])

            self.set_x(values)

            current_result = self.next_x()
            current.append(current_result)

            print("Result: ",learning_data[counter], " : ", current_result)

            new_w = self.weights
            for i in range(len(self.weights)):
                new_w[i] += self.norm * (learning_data[counter] - current_result) * self.values[i]

            counter += 1
        self.weights = new_w

        error = error_func(current, correct_data[self.p::])

        print("Error: ", error)

        return error


perceptron = Perceptron()

correct_data = []
a = 1
b = 1.5

step = (b - a) / 20

for i in range(1, 22):
    correct_data.append(func(a))
    a += step

perceptron.set_w([0, 0, 0, 0, 0])

steps = 0
while perceptron.epoch(correct_data) >= 0.002:
    steps += 1
    print("\n**************** Epoch {number} ****************\n".format(number=steps))
    continue

print("DONE in {steps} steps".format(steps=steps))
