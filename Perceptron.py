import random


def sign(n):
    if (n >= 0):
        return 1
    else:
        return -1


class Perceptron:
    weights = []
    num_of_weights = 2
    lr = 0.05
    def __init__(self):
        for i in range(self.num_of_weights):
            self.weights.append(random.uniform(-1, 1))

    def guess(self, inputs):
        sum = 0
        for i in range(self.num_of_weights):
            sum += inputs[i]*self.weights[i]
        output = sign(sum)
        return output

    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess
        for i in range(self.num_of_weights):
            self.weights[i] += error * inputs[i] * self.lr

