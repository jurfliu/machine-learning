# -*- coding: utf-8 -*-

# @File    : numpy_random_rand_demo.py
# @Date    :  2019-12-13 19:43
# @Author  : admin
#https://blog.csdn.net/u012149181/article/details/78913167
import numpy as np
#案例一  numpy.random.rand(d0,d1,…,dn) ：rand函数根据给定的维度生成[0,1)之间的数据，包含0，但不包含1；dn表示每个表格的维度；返回值为指定维度的数组
r=np.random.rand(4,2);
print(r)
print("*"*50)
r1=np.random.rand(4,3,2);
print(r1);
print("*"*50)
#案例二  numpy.random.randn(d0,d1,…,dn) ：randn函数返回一个或一组样本，具有标准正态分布。dn表示每个表格的维度；返回值为指定维度的数组
#标准正态分布—-standard normal distribution
#标准正态分布又称为u分布，是以0为均值、以1为标准差的正态分布，记为N（0，1）。
r2=np.random.randn() # 当没有参数时，返回单个数据
print(r2)
print("》》》》》》*"*50)
r3=np.random.randn(2,4);
print(r3);
print("*"*50)
r4=np.random.randn(4,3,2)
print(r4);
print("*"*50)
#案例三  3.1 numpy.random.randint(low, high=None, size=None, dtype=’l’)
#返回随机整数，范围区间为[low,high)，包含low，不包含high；参数:low为最小值，high为最大值，size为数组维度大小
#dtype为数据类型，默认的数据类型是np.int
#high没有填写，默认生成随机数的范围是[0,low)
r5=np.random.randint(1,size=5) # 返回[0,1)之间的整数，所以只有0
print(r5);
print("*"*50)
r6=np.random.randint(1,5); ## 返回1个[1,5)时间的随机整数
print(r6)
print("*"*50)
r7=np.random.randint(-5,5,size=(2,2)) #返回【-1 4】之间的数，维度为2*2
print(r7)
print("*"*50)
#  3.2 numpy.random.random_integers(low, high=None, size=None)
#返回随机整数，范围区间为[low,high]，包含low和high
#参数：low为最小值，high为最大值，size为数组维度大小
#high没有填写时，默认生成随机数的范围是[1，low]
#该函数在最新的numpy版本中已被替代，建议使用randint函数
#r8=np.random.random_integers(2,size=5)
#print(r8)
#案例四 生成[0.1)之间的浮点数
''' 
numpy.random.random_sample(size=None)   以给定形状返回[0,1)之间的随机浮点数
numpy.random.random(size=None)
numpy.random.ranf(size=None)
numpy.random.sample(size=None)
'''
print('-----------random_sample--------------')
print(np.random.random_sample(size=(2,2)))

print('-----------random--------------')
print(np.random.random(size=(2,2)))

print('-----------ranf--------------')
print(np.random.ranf(size=(2,2)))
print('-----------sample--------------')
print(np.random.sample(size=(2,2)))
#案例5 numpy.random.choice(a, size=None, replace=True, p=None)
#从给定的一维数组中生成随机数
#参数： a为一维数组,类似数据或整数；size为数组维度；p为数组中的数据出现的概率
#a为整数时，对应的一维数组为np.arange(a)
print('-----------random.choice--------------')
print(np.random.choice(5,3)) #[0,1,2,3,4] 中任意选取3个数
print('-----------random  replace=false--------------')
print(np.random.choice(5, 3, replace=False)); # 当replace为False时，生成的随机数不能有重复的数值
print('-----------random  choice   size=3*2--------------')
print(np.random.choice(5,size=(3,2)))
print('-----------random  choice   list--------------')
demo_list = ['lenovo', 'sansumg','moto','xiaomi', 'iphone']
print(np.random.choice(demo_list,size=(3,3)))
print('-----------random  choice   p--------------')
'''
参数p的长度与参数a的长度需要一致；
参数p为概率，p里的数据之和应为1,p为数组，里面存放选到每个数的可能性，即概率 
'''
demo_list = ['lenovo', 'sansumg','moto','xiaomi', 'iphone']
print(np.random.choice(demo_list,size=(3,3), p=[0.1,0.6,0.1,0.1,0.1]))
#案例六 np.random.seed()的作用：使得随机数据可预测。当我们设置相同的seed，每次生成的随机数相同。如果不设置seed，则每次会生成不同的随机数
#[0.5488135  0.71518937 0.60276338 0.54488318 0.4236548 ]
print(np.random.seed(0))
print(np.random.rand(5))
print('-----------random  seed   p--------------')
#Numpy.random.seed()用来设置随机数生成的随机种子。在seed(n)中，当n的值相同时，生成的随机数相同，其中的n为整数。可理解n为一个标记
print(np.random.seed(18));
print(np.random.rand(5))