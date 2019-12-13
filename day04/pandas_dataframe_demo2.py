import pandas as pd
import numpy as np
dict_data = {   'A': 1,
	             'B': pd.Timestamp('20170426'),
	             'C': pd.Series(1, index=list(range(4)),dtype='float32'),
	             'D': np.array([3] * 4,dtype='int32'),
	             'E': ["Python","Java","C++","C"],
	             'F': 'ITCast' }
print(dict_data);

df_obj2 = pd.DataFrame(dict_data,index=["a","b","c","d"])
print(df_obj2)
#loc和iloc方法
print(df_obj2.iloc[:2])
#loc和iloc方法
print(df_obj2.iloc[:2])
print(df_obj2.iloc[0:3,0:3])
#loc和iloc方法
print(df_obj2.iloc[:2])
print(df_obj2.iloc[0:3,0:3])
print(df_obj2.iloc[[0,1],[0,3]])
#通过loc查看样本数据
print(df_obj2.loc[["a","b"],["A","B"]])
print(df_obj2.loc["a","A"])

