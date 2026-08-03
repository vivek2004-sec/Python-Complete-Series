'''
np.isnan(array)

'''

import numpy as np

arr = np.array([1, 2, np.nan, 3, np.nan, 5])
print(np.isnan(arr))

'''
np.nan_to_num(array)
'''
cleane_arr = np.nan_to_num(arr, nan=100)
print(cleane_arr)