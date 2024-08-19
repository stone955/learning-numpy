"""导入 numpy 库"""

import numpy as np


# 访问数组元素
arr = np.array([1, 2, 3, 4, 5])
print(arr[0], arr[1], arr[-1], arr[3] + arr[4])

# 访问 2-D 数组元素
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2nd element on 1st dim: ", arr[0, 1])
print("2nd element on 2nd dim: ", arr[1, 1])

# 访问 3-D 数组元素
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("2nd element on 1st dim: ", arr[0, 1, 1])
