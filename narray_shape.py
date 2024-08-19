# 数组形状
arr = np.array([1, 2, 3, 4, 5])
print(arr.shape)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr.shape)

arr = np.array([1, 2, 3, 4, 5], ndmin=5)
print(arr)
print(arr.shape)
