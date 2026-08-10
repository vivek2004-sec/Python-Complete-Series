import matplotlib.pyplot as plt
import numpy as np

# Scatter graph = Shows the relationship between two variables helps to identify a correlation (+, -, None)
#                 Example = Study hours vs Test Scores


# Positive Correlation: 
x1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
y1 = np.array([55, 70, 76, 79, 80, 84, 89, 94, 97])


x2 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8])
y2 = np.array([50, 52, 55, 59, 64, 69, 70, 71, 73, 79, 89])
plt.scatter(x1,y1, color='blue', alpha=0.5,
            s = 100, 
            label = 'Class A')
plt.grid()
plt.scatter(x2,y2, color='red', alpha=0.5,
            s = 100, 
            label = "Class B")
plt.title("Result Analysis", fontsize=15)
plt.xlabel("Hours Studied", fontsize=15)
plt.ylabel("Marks", fontsize=15)
plt.legend()
plt.show()