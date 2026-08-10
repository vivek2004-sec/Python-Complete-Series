import matplotlib.pyplot as plt
import numpy as np

# pyplot = gives user friendly interface for plotting.

# x = np.array([2025, 2026, 2027, 2028])
# y = np.array([10, 15, 20, 25])

# plt.plot(x, y)
# plt.show()

std = np.array([[1, 2, 3], [4, 5, 6]])
grade = np.array([[50, 45, 49], [39, 46, 45]])

plt.plot(std,grade)
plt.show()