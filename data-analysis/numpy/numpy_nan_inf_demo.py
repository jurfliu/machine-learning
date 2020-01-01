
# -*- coding: utf-8 -*-

# @File    : numpy_nan_inf_demo.py
# @Date    :  2019-12-30 19:04
# @Author  : admin
import numpy as np
t=np.arange(24).reshape(4,6)
print(t)
print(type(t))
#表达的意思是：矩阵中的元素如果大于20，则替换成1，否则替换成0，相当于三目运算符
c=np.where(t>20,1,0);
print(c)
print("===================裁切======")
#裁切，表达的意思为：小于10则替换成10，大于等于18，则替换成18
d=t.clip(10,18)
print(d)
print("===================设置nan======")
'''
1.nan(NAN,Nan):not a number表示不是一个数字，当我们读取本地的文件为float的时候，如果有缺失，就会出现nan
2.当做了一个不合适的计算的时候(比如无穷大(inf)减去无穷大)
3.两个nan是不相等的
4.nan与任何值计算都为nan
5.判断数字是否为nan，用np.isnan(x)
6.判断含有nan的个数用np.count_nonzero(e!=e)
7.比如，全部替换为0后，替换之前的平均值如果大于0，替换之后的均值肯定会变小，所以更一般的方式是把缺失的数值替换为均值（中值）或者是直接删除有缺失值的一行
'''
#将元素为10的则替换成nan，否则为1,不改变原矩阵中元素的值，而是另开辟一个矩阵将修改后的结果赋值给它
e=np.where(d==10,np.nan,1)
print(e)
print("判断nan的个数",np.count_nonzero(e!=e))
print("判断nan的个数",np.count_nonzero(e[e!=e]))
#设置为判断数据元素是否为nan，对nan赋值，之间修改原矩阵中元素的值
e[np.isnan(e)]=44
print(e)

print("===================设置inf======")
'''
inf(-inf,inf):infinity,inf表示正无穷，-inf表示负无穷,比如一个数字除以0,（python中直接会报错，numpy中是一个inf或者-inf）

'''
e=np.where(d==10,np.inf,1)
print(e)