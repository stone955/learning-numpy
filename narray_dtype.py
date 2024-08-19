"""导入 numpy 库"""

import numpy as np


# 数据类型
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)

arr = np.array([6, 7, 8, 9, 10], dtype="S")
print(arr)
print(arr.dtype)

# 转换已有数组的数据类型
arr = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
newarr = arr.astype("i")
print(arr)
print(arr.dtype)
print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
