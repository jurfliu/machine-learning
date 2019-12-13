#Series是一维数据结构
import pandas as pd
print(pd.Series([1,2,3,4,45]))
s1 = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
print(s1)
print("*"*10)
print(s1.head(3))  #df.head() #默认前10行数据 df.tail() #默认后10 行数据
print(s1.ndim)
print(s1.shape)
print(s1.size)
print(s1.dtype)
print(s1.index) #Index(['a', 'b', 'c', 'd'], dtype='object')
print(s1.values) #[1 2 3 4]
#字典适合构建series
s1=pd.Series(dict(zip(["Apple","pear","banana"],[1,2,3])))
print(s1)
#可以为series增加name属性
s1.name="temp"
print(s1)
s1.index.name="ok"
print(s1.index.name)
#查看series的值
print(s1["Apple"])
print(s1["pear"])