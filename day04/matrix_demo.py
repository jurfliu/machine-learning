#matrix是矩阵，一定是2维的，不能够使用matrix定义超过2维度的数据
#mat是matrix的别名
import numpy as np
mat1 = np.matrix([[1, 2], [3, 4], [5, 6]])
print(mat1)
print(type(mat1))
#matrix
'''
ValueError: matrix must be 2-dimensional
mat1 = np.matrix([[[1, 2], [3, 4], [5, 6]]]) #
print(mat1)
'''


#mat
mat2 = np.mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat2)
mat3=np.mat(np.random.randn(3,3))
print(mat3)
mat4=np.mat("1,2;3,4;5,6")
print(mat4)


print("======")
x = np.random.randint(0, 5, [3, 2, 2])
print(x)
print(x.ndim)   #   三维度
print(x.shape)


