import numpy as np

array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
print(array1 > 4)
print(array1 % 2 == 0)

booleans = np.array([True, True, False, True, True, False, True, True, True, False, True])
print(np.where(booleans))