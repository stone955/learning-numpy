"""导入 numpy 库"""

import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(np.__version__)
print(type(arr))

arr = np.array((6, 7, 8, 9, 10))
print(arr)

# 0-D 数组
arr = np.array(61)
print(arr)

# 1-D 数组
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)

# 2-D 数组
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# 3-D 数组
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr)

# 检查维数
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# 更高维的数组
arr = np.array([1, 2, 3, 4, 5], ndmin=5)
print(arr)
print("number of dimensions: ", arr.ndim)
