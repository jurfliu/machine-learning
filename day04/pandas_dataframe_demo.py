import pandas as pd
import numpy as np
print(pd.DataFrame([1,2,3,4]))
print(pd.DataFrame([[1,2,3,4],[3,5,5,6]]))
#如何添加名字
df1 = pd.DataFrame([[1, 2, 3, 4], [3, 5, 5, 6]], columns=["Apple", "Pear", "Bnanana", "Orange"],
                     index=["a", "b"],dtype="float32")
print(df1)
print(df1.head(1))  #获取前1行
#属性数据有哪些
print(df1.index) #Index(['a', 'b'], dtype='object')
print(df1.columns) #Index(['Apple', 'Pear', 'Bnanana', 'Orange'], dtype='object')
print(df1.shape) #(2, 4)
print(df1.ndim) #2
print(df1.size) #8
print(df1.dtypes)
#取值
print(df1)
print("*"*100)
print(df1["Apple"])
#如果需要对行进行分析
print("》》》"*100)
print(df1.loc[:,"Bnanana"]) #ix()方法已经过时,获取单个banana这一列
print(df1.loc["a","Apple"])
print("*"*100)
print(df1.loc["a":"b","Apple":"Bnanana"])


#增加数据
df1["Pen"]=df1["Apple"]*2
print(df1)
#删除数据列
del df1["Pen"]
print(df1)
'''
df_inner.iloc[:3,:2] #冒号前后的数字不再是索引的标签名称，而是数据所在的位置，从0开始，前三行，前两列。
https://blog.csdn.net/yiyele/article/details/80605909
使用ix按索引标签和位置混合提取数据
df_inner.ix[:‘2013-01-03’,:4] #2013-01-03号之前，前四列数据
loc,iloc和ix，loc函数按标签值进行提取，iloc按位置进行提取，ix可以同时按标签和位置进行提取。
obj.ix[:,val]     #选择单个列
obj.ix[val1,val2] #同时选取行和列
print(df_obj2.ix['A']) #通过ix获取指定索引对应的行信息，ix表示索引字段
print(df_obj2.ix[:,'A'])#选取所有航的指定'A'列的数据

'''