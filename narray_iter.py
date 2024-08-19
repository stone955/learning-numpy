"""导入 numpy 库"""

import numpy as np

# 迭代 1-D 数组
arr = np.array([1, 2, 3, 4, 5])

for a in arr:
    print(a)

# 迭代 2-D 数组
arr = np.array([[1, 2, 3], [4, 5, 6]])

for row in arr:
    print(row)

for row in arr:
    for col in row:
        print(col)

# 迭代 3-D 数组
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for layer in arr:
    print("Layer:", layer)

for layer in arr:
    for row in layer:
        for col in row:
            print(col)

# 使用 nditer() 迭代数组
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)

# 迭代不同数据类型的数组
# 可以使用 op_dtypes 参数，并传递期望的数据类型，以在迭代时更改元素的数据类型。
# NumPy 不会就地更改元素的数据类型（元素位于数组中），因此它需要一些其他空间来执行此操作，
# 该额外空间称为 buffer，为了在 nditer() 中启用它，我们传参 flags=['buffered']。
arr = np.array([1, 2, 3, 4, 5])

for x in np.nditer(arr, flags=["buffered"], op_dtypes=["S"]):
    print(x)

# 以不同的步长迭代
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
    print(x)

# 使用 ndenumerate() 进行枚举迭代
arr = np.array([1, 2, 3, 4, 5, 6])

for idx, x in np.ndenumerate(arr):
    print("idx: ", idx, "x: ", x)

arr = np.array([[1, 2, 3], [4, 5, 6]])

for idx, x in np.ndenumerate(arr):
    print("idx: ", idx, "x: ", x)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for idx, x in np.ndenumerate(arr):
    print("idx: ", idx, "x: ", x)
