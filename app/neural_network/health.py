import numpy as np

average_male = {
    'height': 69, # inches
    'weight': 198, # pounds
    'age': 50, # years
    'bmi': 29.5, # kg/m^2
}

average_female = {
    'height': 63, # inches
    'weight': 170, # pounds
    'age': 50, # years
    'bmi': 29.5, # kg/m^2
}

average_height = average_male['height'] + average_female['height'] / 2
average_weight = average_male['weight'] + average_female['weight'] / 2
average_age = average_male['age'] + average_female['age'] / 2
average_bmi = average_male['bmi'] + average_female['bmi'] / 2

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

class HealthNN:
    """A simple neural network for health predictions."""
    
    def __init__(self, inputs=2, outputs=1, layers=1):
        self.inputs = inputs
        self.outputs = outputs
        self.biases = [np.random.normal()] * (inputs * layers + outputs) # 3
        self.weights = self.biases * inputs # 6
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

x = HealthNN()
print(f"Inputs: {x.inputs}, Outputs: {x.outputs}, Biases: {x.biases}, Weights: {x.weights}") 
# Define dataset
data = np.array([
  [-2, -1],  # Alice
  [25, 6],   # Bob
  [17, 4],   # Charlie
  [-15, -6], # Diana
])
all_y_trues = np.array([
  1, # Alice
  0, # Bob
  0, # Charlie
  1, # Diana
])
print(f"Forward pass output for Alice: {x.forward([-2, -1])}")  # Should print the output for Alice