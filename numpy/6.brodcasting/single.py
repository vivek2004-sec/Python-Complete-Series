''' 
1. Matching dimensions: 

 [1, 2, 3] + [4, 5, 6] = [5, 7, 9]

2. Expanding single elements: 

[1, 2, 3] + 10 = [11, 12, 13]

3. incompatible shapes: 

[1, 2, 3] + [5, 6] = valueerror
'''

import numpy as np

arr = np.array([1, 2, 3])
print(arr*2)



arr1 = np.array([[1,2], [3,4]])
print(arr1.shape)
arr2 = np.array([1,2])
print(arr2.shape)
print(arr1 + arr2)