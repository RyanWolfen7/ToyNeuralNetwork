import numpy as np

def sigmoid(x):
    """Compute the sigmoid activation function."""
    return 1 / (1 + np.exp(-x))

class Neuron:
    """A simple neuron class with weights and bias."""
    
    def __init__(self, weights=np.array([0.0]), bias=0.0):
        self.weights = weights
        self.bias = bias

    def forward(self, inputs):
        """Compute the output of the neuron given input values."""
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)

# Example usage
# weights = np.array([0,1]) # w1 = 0, w2 = 1
# bias = 4
# n = Neuron(weights, bias)

# x = np.array([2, 3]) # x1 = 1, x2 = 2
# print(n.forward(x))  # 0.9990889488055994