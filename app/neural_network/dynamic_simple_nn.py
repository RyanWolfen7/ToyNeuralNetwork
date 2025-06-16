import numpy as np


def sigmoid(x):
    # Sigmoid activation function: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))


def deriv_sigmoid(x):
    # Derivative of sigmoid: f'(x) = f(x) * (1 - f(x))
    fx = sigmoid(x)
    return fx * (1 - fx)


def mse_loss(y_true, y_pred):
    # y_true and y_pred are numpy arrays of the same length.
    return ((y_true - y_pred) ** 2).mean()


class Dynamic_Simple_NN:
    """A simple neural network for health predictions."""

    def __init__(self, inputs=2, outputs=1, layers=1):
        self.inputs = inputs
        self.outputs = outputs
        self.biases = [np.random.normal()] * (inputs * layers + outputs)  # 3
        self.weights = self.biases * inputs  # 6

    def forward(self, x):
        total_nodes = len(self.biases)
        hidden_nodes = []

        # Process input layer to hidden layer
        for i in range(total_nodes - self.outputs):
            weight_sum = 0
            for j in range(self.inputs):
                weight_idx = i * self.inputs + j
                weight_sum += self.weights[weight_idx] * x[j]
            weight_sum += self.biases[i]
            hidden_nodes.append(sigmoid(weight_sum))

        # Process hidden layer to output
        output = 0
        for i in range(len(hidden_nodes)):
            weight_idx = len(self.weights) - len(hidden_nodes) + i
            output += hidden_nodes[i] * self.weights[weight_idx]
        output += self.biases[-1]

        return sigmoid(output)
