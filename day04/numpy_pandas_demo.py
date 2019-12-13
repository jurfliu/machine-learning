# -*- coding: utf-8 -*-

# @File    : numpy_pandas_demo.py
# @Date    :  2019-12-13 18:06
# @Author  : admin
import numpy as np
import pandas as pd
r=np.random.randn(3); #randn函数返回一个或一组样本，具有标准正态分布。
print(r)
print("#"*50);
df_data = pd.DataFrame([np.random.randn(3), [1., 2., np.nan],
                        [np.nan, 4., np.nan], [1., 2., 3.]])
print(df_data.head())
# is_null
print(df_data.isnull())
# dropna
df2 = df_data.dropna(axis=0) #行
df3 = df_data.dropna(axis=1) #列
'''
pandas的设计目标之一就是使得处理缺失数据的任务更加轻松些。pandas使用NaN作为缺失数据的标记。
使用dropna使得滤除缺失数据更加得心应手。
'''
print(df2)
print("***"*40)
print(df3)
# fillna
df4=df_data.fillna(100)
print(df4)
# abs--直接使用numpy函数,abs绝对值
print(np.abs(df_data))
print("--"*60);
# apply
print(df4.apply(lambda x:x.max(),axis=1))
'''
在Python中如果想要对数据使用函数，可以借助apply(),applymap(),map() 来应用函数
当我们要对数据框（DataFrame）的数据进行按行或按列操作时用apply()
df1.apply(lambda x :x.max(),axis=1)
#axis=1，表示按行对数据进行操作#从下面的结果可以看出，我们使用了apply函数之后，系统自动按行找最大值
'''
