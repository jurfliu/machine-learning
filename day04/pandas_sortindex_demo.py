# -*- coding: utf-8 -*-

# @File    : pandas_sortindex_demo.py
# @Date    :  2019-12-19 17:14
# @Author  : admin
import numpy as np
import pandas as pd
s1=pd.Series(np.random.randn(12),index=[
    ["a","a","a","b","b","b","c","c","c","d","d","d"],[0,1,2,0,1,2,0,1,2,0,1,2]
])
print(s1)
print("访问外层========")
#访问外层索引的值
print(s1["a"])
print("====s1[a,1]====")
print(s1["a",1])
print(s1[:,1])
#交换内外层索引
print("====交换=====")
print(s1.swaplevel())
print(s1.swaplevel().sort_index())
