import matplotlib.pyplot as plt
import numpy as np

# Scatter graph = Shows the relationship between two variables helps to identify a correlation (+, -, None)
#                 Example = Study hours vs Test Scores

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([55, 70, 76, 79, 80, 84, 89, 94, 97])

plt.scatter(x,y, color='skyblue', alpha=0.5,
            s = 100)
plt.title("Result Analysis", fontsize=15)
plt.xlabel("Hours Studied", fontsize=15)
plt.ylabel("Marks", fontsize=15)
plt.show()