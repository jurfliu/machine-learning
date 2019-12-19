# -*- coding: utf-8 -*-

# @File    : numpy_pandas_query_demo.py
# @Date    :  2019-12-19 17:53
# @Author  : admin
from numpy.random import randn
from pandas import DataFrame
df = DataFrame(randn(10, 2), columns=list('ab'))#【“a”,"b"】
print(df)
print("=======================")
print(df.query('a > b'))
print(">>>=======================")
print(df.a > df.b)

print("和query同样的功能=======================")
print(df[df.a > df.b])