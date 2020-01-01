# -*- coding: utf-8 -*-

# @File    : nump_function_demo.py
# @Date    :  2019-12-31 17:00
# @Author  : admin
import numpy as np
'''
标准差是一组数据平均值分散程度的一种度量。一个较大的标准差，代表大部分数值和其平均值之间差异较大；一个较小的标准差，代表这些数值较接近平均值
反映出数据的波动稳定情况，越大表示波动越大，约不稳定
'''
#将一维转成多维度
r=np.arange(0,32).reshape(8,4)
print(r)
'''
默认返回多维数组的全部的统计结果,如果指定axis则返回一个当前轴上的结果
'''
d=r.sum(axis=None)
print(d)
#按行
d=r.sum(axis=1)
print(d)
print("#########################均值################")
a=r.mean(axis=0);
print(a)
print("#########################标准差################")
b=r.std(axis=None);
print(b)
'''
求和：t.sum(axis=None)
均值：t.mean(a,axis=None)  受离群点的影响较大
中值：np.median(t,axis=None) 
最大值：t.max(axis=None) 
最小值：t.min(axis=None)
极值：np.ptp(t,axis=None) 即最大值和最小值只差
标准差：t.std(axis=None) 
'''
