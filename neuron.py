import numpy as np

def sigmoid(x):
    # Activation function: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias

    def feedforward(self, inputs):
        # Weight inputs, add bias, then use activation function in sigmoid
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)
