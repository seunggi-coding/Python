# numpy 기본 연산

import numpy as np

array1 = np.arange(10)
array2 = np.arange(10, 20)

print(array1)
print(array2)

print(array1 * 2)
print(array1 / 2)
print(array1 + 2)
print(array1 ** 2)
print(array1)

# 같은 순서의 열끼리 연산도 가능
print(array1 + array2)