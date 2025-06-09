import numpy as np
from app.neural_network.neuron import Neuron

class TestNeuralNetwork:
    """A simple neural network class for testing purposes."""
    def __init__(self):
        weights = np.array([0,1])
        bias = 0

        self.h1 = Neuron(weights, bias)
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)
    
    def forward(self, x):
        """Compute the output of the neural network given input values."""
        h1_output = self.h1.forward(x)
        h2_output = self.h2.forward(x)
        o1_output = self.o1.forward(np.array([h1_output, h2_output]))
        return o1_output

# Example usage
# network = TestNeuralNetwork()
# x = np.array([2, 3])  # 0.7216325609518421
# print(network.forward(x))  # Output of the neural network
# # This should print the output of the neural network given the input x