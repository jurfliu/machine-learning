# -*- coding: utf-8 -*-

# @File    : pandas_read_file_demo.py
# @Date    :  2019-12-19 18:04
# @Author  : admin
import pandas as pd
df_love=pd.read_csv("e:/SklearnTest.txt")
print(df_love)
#各种属性
print(df_love.shape) #(9, 6)
print(df_love.ndim) #2
print(df_love.size) #54
print(df_love.dtypes)
print(df_love.info())
print("查询");
train_data=df_love.query("is_date != -1")
print(train_data)

test_data=df_love.query("is_date == -1")
print(test_data)

df2=df_love.drop(labels="is_date",axis=1) #axis=1表示列
print(df2)