import matplotlib.pyplot as plt 
import numpy as np


# histogram = A visual representation of distribution of quantitative data.
            #   They group values into bins(intervals.)
            #   and counts how many falls in each range.
        
        
scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores, 0, 100)
plt.hist(scores, bins=20)
plt.show()