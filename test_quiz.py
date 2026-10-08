import numpy as np

y = np.array([[1.0], [2.0], [3.0], [4.0], [5.0]])
y_fit = np.array([1.1, 1.9, 3.2, 3.9, 5.1])
residual = y - y_fit

print(residual.shape)