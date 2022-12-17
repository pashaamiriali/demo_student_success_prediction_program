import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


class Network:
    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights = 2 * np.random.random((10, 1)) - 1

    def train(self, training_inputs, training_outputs, training_iterations):
        for _ in range(training_iterations):
            output = self.think(training_inputs)
            error = training_outputs - output
            adjustments = np.dot(training_inputs.T, error *
                                 sigmoid_derivative(output))
            self.synaptic_weights += adjustments

    def think(self, inputs):
        inputs = inputs.astype(float)
        output = sigmoid(np.dot(inputs, self.synaptic_weights))
        return output

    def get_synaptic_weights(self):
        return np.array(self.synaptic_weights)

