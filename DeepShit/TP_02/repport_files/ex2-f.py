import numpy as np
import matplotlib.pyplot as plt

def c1(x):
    return (1 / (1 + np.exp(-x)) - 1)**2

x = np.linspace(-5, 5, 1000)
y = c1(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('c1(x)')
plt.show()