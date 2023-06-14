import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoidGradient(z):
    return sigmoid(z) * (1 - sigmoid(z))

z = np.arange(-10, 10, 0.1)
plt.plot(z, sigmoid(z), 'r')
plt.plot(z, sigmoidGradient(z), 'b')
plt.show()