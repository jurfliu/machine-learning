# -*- coding: utf-8 -*-

# @File    : knn-demo.py
# @Date    :  2019-12-28 19:02
# @Author  : admin

# -*- coding: utf-8 -*-

# @File    : sk-learn-knn-demo.py
# @Date    :  2019-12-28 11:51
# @Author  : admin

from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
"""
 K-近邻预测用户签到位置
 :return:None
 ########################。。。KNN。。。#####
 1.导入类库：from sklearn.neighbors import KNeighborsClassifier                             

2. 创建数据

3.创建对象:  knn = KNeighborsClassifier(n_neighbors=3)(注:n_neighbors 就是 kNN 里的 k，就是在做分类时，我们选取问题点最近的多少个最近邻)

4.训练数据: knn.fit(x_train,y_train)
5.预测数据: knn.predict(x_test)
6.评测数据:knn.score(x_test,y_tes
############################   本程序逻辑  #######
数据预处理
   缩小数据集范围
     时间特征提取
     将签到数少于n的位置删除
数据集划分
特征工程
    标准化
KNN算法
GSCV优化
模型评估
 """
def myknnDemo():
    # 读取数据
    data = pd.read_csv("../data/knn-train.csv")
    #print(data)
    #print(data.head(10))
    # 处理数据
    # 1、缩小数据,查询数据晒讯,缩小数据集范围 DataFrame.query()
    data = data.query("x > 2.0 &  x < 8.25 & y > 2.5 & y < 8.75")
    print(data)
    print(data.shape)
    # 处理时间的数据  用 pandas 的to_datetime 方法，把 "date" 列的字符类型数据解析成 datetime 对象。
    time_value = pd.to_datetime(data['time'], unit='s')
    print(time_value)
    # 把日期格式转换成 字典格式,pd.DatetimeIndex()时间戳索引：直接把时间序列变成时间戳索引
    #.to_datetime仅转换格式，.DatetimeIndex还能设置为索引,https://www.jianshu.com/p/4ece5843d383
    time_value = pd.DatetimeIndex(time_value)
    print(time_value)
    print(time_value.day)
    print(data)

#调用执行
myknnDemo();