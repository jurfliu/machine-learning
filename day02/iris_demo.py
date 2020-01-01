# -*- coding: utf-8 -*-

# @File    : iris_demo.py
# @Date    :  2019-12-24 21:56
# @Author  : admin
'''
load*和fetch*返回的数据类型datasets.base.Bunch(字典格式)

data：特征数据数组，是 [n_samples * n_features] 的二维
	          numpy.ndarray 数组

target：标签数组，是 n_samples 的一维 numpy.ndarray 数组

DESCR：数据描述

feature_names：特征名,新闻数据，手写数字、回归数据集没有

target_names：标签名,回归数据集没有
'''
from sklearn.datasets import  load_iris
r=load_iris();
print("========特征数据数组，是 [n_samples * n_features] 的二维numpy.ndarray 数组==========")
print(r.data)
print("========标签数组，是 n_samples 的一维 numpy.ndarray 数组==========")
print(r.target)
print("========数据描述==========")
print(r.DESCR);
print("========特征名==========")
print(r.feature_names)
print("========标签名==========")
print(r.target_names)
print(r.data.shape);
print("=========================================================================================================")

from sklearn.datasets import load_digits
digits = load_digits()
print(digits.data.shape)
print(digits.target)
print(digits.target_names);
#print(digits.images);



