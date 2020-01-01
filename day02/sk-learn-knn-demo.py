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
    data = pd.read_csv("./data/train.csv")
    print(data.head(10))
    # 处理数据
    # 1、缩小数据,查询数据晒讯,缩小数据集范围 DataFrame.query()
    data = data.query("x > 1.0 &  x < 1.25 & y > 2.5 & y < 2.75")
    # 处理时间的数据
    time_value = pd.to_datetime(data['time'], unit='s')
    print(time_value)
    # 把日期格式转换成 字典格式
    time_value = pd.DatetimeIndex(time_value)
    # 构造一些特征
    data['day'] = time_value.day
    data['hour'] = time_value.hour
    data['weekday'] = time_value.weekday
    # 把时间戳特征删除
    data = data.drop(['time'], axis=1)
    print(data)
    # 把签到数量少于n个目标位置删除
    place_count = data.groupby('place_id').count()

    tf = place_count[place_count.row_id > 3].reset_index()

    data = data[data['place_id'].isin(tf.place_id)]
    # 取出数据当中的特征值和目标值
    y = data['place_id']
    x = data.drop(['place_id'], axis=1)
    print("================================== knn开始 ===============");
    # 进行数据的分割训练集合测试集，train_test_split：交叉验证：将拿到的训练数据，分为训练集、验证集和测试集。
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    # 特征工程（标准化）
    std = StandardScaler()
    # 对测试集和训练集的特征值进行标准化
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)
    # 进行算法流程 # 超参数
    knn = KNeighborsClassifier()

    # # fit， predict,score
    # knn.fit(x_train, y_train)
    #
    # # 得出预测结果
    # y_predict = knn.predict(x_test)
    #
    # print("预测的目标签到位置为：", y_predict)
    #
    # # 得出准确率
    # print("预测的准确率:", knn.score(x_test, y_test))

