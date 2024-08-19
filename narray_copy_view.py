"""导入 numpy 库"""

import numpy as np


# 数组副本
arr = np.array([1, 2, 3, 4, 5])
newarr = arr.copy()
arr[0] = 10
print(arr)
print(newarr)

# 数组视图
arr = np.array([1, 2, 3, 4, 5])
newarr = arr.view()
arr[0] = 10
newarr[1] = 9
print(arr)
print(newarr)

# 检查数组是否拥有数据
arr = np.array([1, 2, 3, 4, 5])
newarr = arr.view()
print(arr.base)
print(newarr.base)
