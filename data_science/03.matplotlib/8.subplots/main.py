import matplotlib.pyplot as plt
import numpy as np


# Figure = The entire canvas
# Ax = A single plot (subplot)

x = np.array([1, 2, 3, 4, 5])

y = np.array([7, 8, 9, 9, 4])

figure, axes = plt.subplots(2, 2)
axes[0, 0].plot(x, x*2)
axes[0, 0].set_title("x*2", color='red')

axes[0, 1].plot(x, y)
axes[0, 1].set_title('x, y', color='red')

plt.show()