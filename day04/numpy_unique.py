import  numpy as np
arr1 = np.array([[1, 2, 3], [4, 4, 6], [7, 8, 9]])
print(arr1)
print(np.any(arr1>0))
print(np.all(arr1>0))
#unique函数
print(np.unique(arr1)) #sorted unique