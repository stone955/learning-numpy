"""导入 numpy 库"""

import numpy as np

# 拆分 NumPy 数组
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
newarr = np.array_split(arr, 3)

print(newarr)

# 如果数组中的元素少于要求的数量，它将从末尾进行相应调整。
arr = np.array([1, 2, 3, 4, 5])
newarr = np.array_split(arr, 3)

print(newarr)

# 如果将一个数组拆分为 3 个数组，则可以像使用任何数组元素一样从结果中访问它们。
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

# 分割二维数组
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 2)

print(newarr)

# 把这个 2-D 拆分为三个 2-D 数组。
arr = np.array(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
)
newarr = np.array_split(arr, 3)

print(newarr)

# 沿行把这个 2-D 拆分为三个 2-D 数组。
arr = np.array(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
)
newarr = np.array_split(arr, 3, axis=1)

print(newarr)

# 使用 hsplit() 方法将 2-D 数组沿着行分成三个 2-D 数组。
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)

print(newarr)