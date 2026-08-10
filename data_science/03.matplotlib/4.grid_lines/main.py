import matplotlib.pyplot as plt
import numpy as np

# grid() = Helps make plots easier to read by adding reference lines.


x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 10, 25]

plt.grid(axis='both', linewidth=2, linestyle = 'dashed')
plt.plot(x,y, marker='.', 
         markersize=10)
plt.show()