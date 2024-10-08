import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x_value = np.linspace(-10, 10, 400) #-10 ~ 10 랜덤값 400개
y_value = sigmoid(x_value)

plt.figure(figsize= (8, 6))
plt.plot(x_value, y_value)
plt.xlabel('x')
plt.grid(True)
plt.legend()
plt.show()