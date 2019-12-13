# -*- coding: utf-8 -*-

# @File    : numpy_array_demo.py
# @Date    :  2019-11-28 15:03
# @Author  : admin
'''
1.ndim属性：维度个数
2.shape属性：维度原组
3.dtype属性：数据类型
'''
import numpy as np
#进一步学习矩阵或数组的创建
arr1 = np.array([1, 2, 3, 4,5])
arr2 = np.array((1, 2, 3, 4))
arr3 = np.array({1, 2, 3, 4})
print(arr1)
print(arr2)
print(arr3)
print(type(arr3))
#属性ndim-shape-size
print(arr1.ndim) #1   ndim返回的是数组的维度，返回的只有一个数，该数即表示数组的维度。
print(arr1.shape) #(4,) shape：表示各位维度大小的元组。返回的是一个元组。因为arr1.ndim维度为1，元组内只返回一个数。一维按个数计算，为5
print(arr1.size) #4   数据个数
#二维度矩阵
arr4=np.array([[1,2,3],[3,4,5],[4,5,6]])
print(arr4)
# [[1 2 3]
#  [3 4 5]
#  [4 5 6]]
print(arr4.ndim) #2
print(arr4.shape) #3 3    二维计算几行几列《》
print(arr4.size) #3*3=9
#三维度
arr5=np.array([[[1,2],[3,4],[5,6]]],dtype="float32")
print(arr5)
print(arr5.ndim) #3
print(arr5.shape) #[A]  A=[[1,2],[3,4],[5,6]]  A=[b,c,d] b=[1,2],c=[3,4],d=[5,6]   ===>（1,3,2）

#全为0矩阵
print(np.zeros(shape=(3,3)))
#全为1矩阵
print(np.ones(shape=(3,3)))
#等差数列
print(np.linspace(1,10,10))
#等比数列
print(np.logspace(1,10,10))
#对角阵
print(np.diag([1,2,3]))