import numpy as np
arr1 = np.array(np.random.randn(5, 5))#5行5列当函数括号内有两个及以上参数时，则返回对应维度的数组，能表示向量或矩阵；
print(arr1)
# np.ceil(): 向上最接近的整数，参数是 number 或 array
#print(np.ceil(arr1))
# np.floor(): 向下最接近的整数，参数是 number 或 array
#print(np.floor(arr1))
# np.rint(): 四舍五入，参数是 number 或 array
#print(np.rint(arr1))
# np.isnan(): 判断元素是否为 NaN(Not a Number)，参数是 number 或 array
#print(np.isnan(arr1))
# np.multiply(): 元素相乘，参数是 number 或 array
#print(np.multiply(np.array([[1,2],[3,4]]),np.array([[1,2],[3,4]])))
# np.divide(): 元素相除，参数是 number 或 array
# np.abs()：元素的绝对值，参数是 number 或 array
#print(np.abs(arr1))
# np.where(condition, x, y): 三元运算符，x if condition else y
print(np.where(arr1>0,1,-1))