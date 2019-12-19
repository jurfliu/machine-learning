# -*- coding: utf-8 -*-

# @File    : numpy_pandas_dataframe_demo.py
# @Date    :  2019-12-19 17:29
# @Author  : admin
import  pandas as pd
import  numpy as np
df1 = pd.DataFrame(np.random.randn(5, 4), columns=["a", "b", "c", "d"])
print(df1)
print(df1.sum(axis=0)) #按列统计
print(df1.sum(axis=1)) #axis=1按行统计

print(df1.mean(axis=0))
print("=======按行求平均值:===")
print(df1.mean(axis=1))

print("=======按列求标准差值:===")
print(df1.std(axis=0))
print("=======按行求标准差值:===")
print(df1.std(axis=1))

print("=======describe:===")
#decsription  pandas的describe可以用来展示数据的一些描述性统计信息
print(df1.describe())