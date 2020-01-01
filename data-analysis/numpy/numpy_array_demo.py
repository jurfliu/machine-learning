# -*- coding: utf-8 -*-

# @File    : numpy_array_demo.py
# @Date    :  2019-12-30 15:29
# @Author  : admin
import numpy as np
'''
数组的结构：array.shape
数组的维度：array.ndim
元素的类型：array.dtype
数组元素的个数：array.size
数组的索引（下标）:array[0]
'''
########################################################1.1 定义numpy的数组##########################
a=np.array([1,2,3,4,5,6])
b=np.array(range(10))    ## np.arange(起始值, 结束值, 步长（默认1）)
#arange 可以设置起始，结束值，步长
b = np.arange(1, 10, 3)
c=np.arange(1,7);
print(a)
print(b)
print(c)
#元素的类型
print(a.dtype)
#数组元素的个数
print(a.size)
#维度
print(a.ndim)
#数组的结构
print(a.shape)
print(type(a))
'''
[1 2 3 4 5 6]
[1 2 3 4 5 6 7 8 9]
[1 2 3 4 5 6]
int32
6
1
(6,)
<class 'numpy.ndarray'>
'''
########################################################1.2 修改numpy的数组类型##########################
a=np.array([1,0,1,0],dtype=np.bool)
print(a)
#修改数据类型
a=a.astype(np.int)
print(a)
b=np.array([0.34567,0.23678])
#四舍五入，保留小数
b=np.round(b,2)
print(b)
'''
[ True False  True False]
[1 0 1 0]
[0.35 0.24]
'''
########################################################1.3 修改numpy的数组类型##########################
a=np.array([34,5,6,7,8,9,0])
print(a.shape)   #shpe有几个值就是几维
b=np.array([[2,4,1,5,6,1],[9,5,76,23,5,9]])
#查看数组的形状
print(b.shape)
#修改数组的形状
c=b.reshape(3,4);
print(c)
print(b.shape)
print(c.shape)
#数组转成一维
d=c.reshape(1,12);
print(d)
print(d.shape) #还是二维的
#正确的语法,转成一维
print(b.flatten())
########################################################1.4 numpy数组的计算##########################
'''
如果两个数组的后缘维度，(即从末尾开始算起的维度)，的轴长度相符或其中一方的长度为1
，则认为他们是广播兼容的，广播会在缺失和（长度为1）的维度上进行
'''
a=np.array([[3,4,5,6,7,8],[1,2,3,4,5,6]])  #(2,6)
b=np.array([[5,6,7,8,9,0],[9,8,7,6,5,7]])
c=np.array([1,2,3,4,5,8])  #(6,)
print("======")
print(a+1);
print(a*2)
print(a+b)
print(a+c)
'''
======
[[4 5 6 7 8 9]
 [2 3 4 5 6 7]]
[[ 6  8 10 12 14 16]
 [ 2  4  6  8 10 12]]
[[ 8 10 12 14 16  8]
 [10 10 10 10 10 13]]
[[ 4  6  8 10 12 16]
 [ 2  4  6  8 10 14]]

'''