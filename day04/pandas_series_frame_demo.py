# -*- coding: utf-8 -*-

# @File    : pandas_series_frame_demo.py
# @Date    :  2019-12-12 18:02
# @Author  : admin
import pandas as pd
s1=pd.Series(range(11),index=range(11))  #索引(从0到N-1)
s2=pd.Series(range(5),index=range(5)) # range(1,5) #代表从1到5(不包含5) ; range(1,5,2) #代表从1到5，间隔2(不包含5); range(5) #代表从0到5(不包含5)
print("S1:",s1)
print("-"*50)
print("S2:",s2)
print("*"*50)
print("S1+S2:",s1+s2)
print("!"*50)
print(s1.add(s2,fill_value=100))  #fill_value将s1与s2相加时，s1为NaN的值替换为100，再加上+s1的原值
#注意：缺失值NaN与任何值相加的结果均为NaN，所以这就是为什么要用到fill_value的原因啦
print("==============")
import numpy as np
p=np.ones((3,3));#ones()返回一个全1的n维数组
print(p)
df1=pd.DataFrame(np.ones((3,3)),columns=["a","b","c"])
df2=pd.DataFrame(np.ones((2,2)),columns=["a","b"])
print(df1)
print(df2)
print(df1+df2)
print(df1.add(df2,fill_value=100))
