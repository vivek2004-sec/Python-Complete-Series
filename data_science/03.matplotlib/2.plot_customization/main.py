import matplotlib.pyplot as plt
import numpy as np


x = np.array([2025, 2026, 2027, 2028])
y1 = np.array([10, 15, 20, 15])
y2 = np.array([12, 23, 26, 18])

# plt.plot(x, y1, marker='.', markersize=10, markerfacecolor='#8a080f', markeredgecolor='#f542b0',
#          linestyle='solid',
#          linewidth = 1,
#          color='#171617')

# plt.plot(x, y2, marker='.', markersize=10, markerfacecolor='#8a080f', markeredgecolor='#f542b0',
#          linestyle='solid',
#          linewidth = 1,
#          color='#171617')

line_style = dict(marker='.', markersize=10, markerfacecolor='#8a080f', markeredgecolor='#f542b0',
         linestyle='solid',
         linewidth = 1,
         color='#171617')

plt.plot(x,y1, **line_style)
plt.plot(x,y2, **line_style)
plt.show()
