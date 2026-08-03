#  Reshaping = changing the dimensions of the array without modifying the data inside it.
#  The number of elements in the array will still be the same even after reshaping the array.
#  reshaping does not create a copy it creates a view. 
"""
.reshape(rows, columns)   
    
"""

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = array.reshape(2, 3)
print(reshaped_arr)


# Flattening: 

# .ravel() --> view 
# .flatten() --> copy


arr = np.array([[1, 2, 3], 
                [4, 5, 6]])
print(arr.ravel())
print(arr.flatten())