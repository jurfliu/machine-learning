# -*- coding: utf-8 -*-

# @File    : love_story.py
# @Date    :  2019-11-27 18:56
# @Author  : admin
import pandas as pd
love_file=pd.read_csv("./SklearnTest.txt")
#加载文件内容
print(love_file)
#查看文件结构
print(love_file.info())
print(love_file.index) #RangeIndex(start=0, stop=9, step=1)
#查看列名
print(love_file.columns)