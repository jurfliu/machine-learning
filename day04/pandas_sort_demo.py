# -*- coding: utf-8 -*-

# @File    : pandas_sort_demo.py
# @Date    :  2019-12-13 18:53
# @Author  : admin
import numpy as np
import pandas as pd
'''
dataFram函数中第一个参数：数据，第二个为：行的索引，第三个为：列的索引
'''
df4 = pd.DataFrame(np.random.randn(3, 5),  #randn()  正态分布
		                   index=np.random.randint(3, size=3),
		                   columns=np.random.randint(5, size=5))
print(df4)
df4_isort = df4.sort_index(axis=1, ascending=False)  #按列降序排列
print(df4_isort) # 4 2 1 1 0
'''
作用：默认根据行标签对所有行排序，或根据列标签对所有列排序，或根据指定某列或某几列对行排序。
注意：df. sort_index()可以完成和df. sort_values()完全相同的功能，但python更推荐用只用df. sort_index()对“根据行标签”和“根据列标签”排序，其他排序方式用df.sort_values()。
调用方式
sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, by=None)
axis：0按照行名排序；1按照列名排序
level：默认None，否则按照给定的level顺序排列---貌似并不是，文档
ascending：默认True升序排列；False降序排列
inplace：默认False，否则排序之后的数据直接替换原来的数据框
kind：排序方法，{‘quicksort’, ‘mergesort’, ‘heapsort’}, default ‘quicksort’。似乎不用太关心。
na_position：缺失值默认排在最后{"first","last"}
by：按照某一列或几列数据进行排序，但是by参数貌似不建议使用

作者：马尔代夫Maldives
链接：https://www.jianshu.com/p/f0ed06cd5003
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''