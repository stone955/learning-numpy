"""导入 numpy 库"""

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# 使用 concatenate() 函数进行数组拼接
arr = np.concatenate((arr1, arr2))

print(arr)

# 沿着行 (axis=1) 连接两个 2-D 数组
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

# 使用堆栈函数连接数组
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2))

print(arr)

# 沿着列 (axis=1) 连接两个 2-D 数组
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)

# 沿行堆叠
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.hstack((arr1, arr2))

print(arr)

# 沿列堆叠
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.vstack((arr1, arr2))

print(arr)

# 沿高度堆叠
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)