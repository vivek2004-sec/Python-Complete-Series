import matplotlib.pyplot as plt
import numpy as np

x = np.array([2025, 2026, 2027, 2028])
y1 = np.array([10, 15, 20, 15])
y2 = np.array([12, 23, 26, 18])
y3 = np.array([1, 13, 6, 28])

plt.title("Class Size", fontsize=20,
                        family='Arial',
                        fontweight='bold',
                        color="#4129c6")
plt.xlabel("Year", fontsize=15, 
                    family="Arial",
                    fontweight='bold',
                    color="#3189b8")

plt.ylabel("Students", fontsize=15, 
                    family="Arial",
                    fontweight='bold'
                    , color='#3189b8')
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xticks(x)

plt.show()