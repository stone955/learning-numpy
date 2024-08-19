"""导入 numpy 库"""

import numpy as np


# 数组裁切
arr = np.array([1, 2, 3, 4, 5])
print(arr[1:5])
print(arr[2:])
print(arr[:3])
print(arr[1:5:2])
print(arr[::2])

# 裁切 2-D 数组
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])
print(arr[0:2, 1:4])
