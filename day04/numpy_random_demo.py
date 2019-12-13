# -*- coding: utf-8 -*-

# @File    : numpy_random_demo.py
# @Date    :  2019-11-28 11:57
# @Author  : admin
import numpy as np
#1.给定上下限范围内选取整数
x=np.random.randint(0,100,size=(1,10))  #(前两个参数指定数据的范围(0,100),size指定1行10列
y=np.random.randint(0,10,7) #(前面两个参数指定数据的范围0,10),0-10之间的7个数
print("x",x);
print("y",y);
#2.生成随机浮点数
n1=np.random.random((4,5)) #生成4行5列的浮点数，浮点数都是从0-1中随机。
print("n1",n1)
#3.正态分布的随机样本数
n2=np.random.randn(4,4) #生成一个4行4列浮点数或N维浮点数组，取数范围：正态分布的随机样本数。
print("n2",n2)
#4.产生[0,1)中均匀分布的样本值
z=np.random.uniform(-1, 5, size = (3, 4)) # 'size='可省略，（0,1）之间的均匀分布
print("z:",z);
#5.产生二项分布的样本值
n, p = 10, .5  # number of trials, probability of each trial试验次数，每次试验的概率
s = np.random.binomial(n, p, 1000) #产生二项分布的样本值
print("s",s)
#6.产生高斯分布的样本值
k=np.random.normal(0,1,10) #参数顺序：1.均值 2.标准差 3.生成多少样本
print("k",k)
#7.产生卡方分布的样本值
s = np.random.chisquare(2,size=(2,3)) #2为自由度
print("s",s)