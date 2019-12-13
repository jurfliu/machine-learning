'''

 np.mean(), np.sum()：所有元素的平均值，所有元素的和，参数是 number 或 array
# 	np.max(), np.min()：所有元素的最大值，所有元素的最小值，参数是 number 或 array
# 	np.std(), np.var()：所有元素的标准差，所有元素的方差，参数是 number 或 array
# 	np.argmax(), np.argmin()：最大值的下标索引值，最小值的下标索引值，参数是 number 或 array
# 	np.cumsum(), np.cumprod()：返回一个一维数组，每个元素都是之前所有元素的 累加和

'''
import numpy as np
#一定要注意分析数据的时候按照行or列进行
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(np.sum(arr1,axis=1)) #行
print(np.sum(arr1,axis=0)) #列
print(np.mean(arr1,axis=0))
print(np.mean(arr1,axis=1))
print(np.max(arr1,axis=1))
print(np.max(arr1,axis=0))
print(np.std(arr1,axis=1))
print(np.var(arr1,axis=1))
print(np.argmax(arr1,axis=0))
print(np.argmin(arr1,axis=0))
print(np.cumsum(arr1))
print(np.cumsum(arr1,axis=0))