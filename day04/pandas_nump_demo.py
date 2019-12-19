# -*- coding: utf-8 -*-

# @File    : pandas_nump_demo.py
# @Date    :  2019-12-19 16:11
# @Author  : admin
import numpy as np
import pandas as pd

df_data = pd.DataFrame([np.random.randn(3), [1., 2., np.nan],
                        [np.nan, 4., np.nan], [1., 2., 3.]])
print("----df-data------")
print(df_data.head())
print(df_data.shape)
# is_null  判断是否有缺失值数据
print(df_data.isnull())
# dropna  pandas使用NaN作为缺失数据的标记。通过**dropna()**滤除缺失数据：
df2 = df_data.dropna(axis=0) #行
df3 = df_data.dropna(axis=1) #列
print("-----df2-----")
print(df2)
print(df3)
# fillna 填充/替换缺失数据
df4=df_data.fillna(100)
print(df4)

# abs--直接使用numpy函数
print("----缺失值填补 -----");
print(np.abs(df_data))
# apply  dataframe.apply(function,axis)对一行或一列做出一些操作（axis=1则为对某一行进行操作，此时，apply函数每次将dataframe的一行传给function，然后获取返回值，将返回值放入一个series）
print("----apply-----");
f=lambda x:x.max();
print(df4.apply(f,axis=1));#将一行的数据输入进去，求出最大值，然后输出