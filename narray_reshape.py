"""导入 numpy 库"""

import numpy as np


# 从 1-D 重塑为 2-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
# 检查重塑后的数组是副本还是视图
print(newarr.base)

# 展平数组
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)
