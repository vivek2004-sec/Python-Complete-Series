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

'''
np.isinf()
'''
array = np.array([2, 3, np.inf, 5, -np.inf, 7])
print(np.isinf(array))

cleaned_array = np.nan_to_num(array, posinf=1000, neginf=-1000)
print(cleaned_array)