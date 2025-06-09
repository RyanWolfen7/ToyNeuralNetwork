import numpy as np
from app.neural_network.dynamic_simple_nn import Dynamic_Simple_NN

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


# Testing the Dynamic_Simple_NN class
x = Dynamic_Simple_NN()
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