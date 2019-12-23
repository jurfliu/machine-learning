# -*- coding: utf-8 -*-

# @File    : k-m.py
# @Date    :  2019-12-18 23:34
# @Author  : admin
'''
这个k-means算法完整
从数据读取，标准化，聚类，输出结果
https://blog.csdn.net/sinat_25873421/article/details/80641286
'''
import pandas as pd
import matplotlib.pyplot as plt
#参数初始化
inputfile = 'e:/consumption_data.xls' #销量及其他属性数据
outputfile = 'e:/data_result.xls' #保存结果的文件名
k = 3 #聚类的类别
iteration = 500 #聚类最大循环次数
data = pd.read_excel(inputfile, index_col = 'Id') #读取数据
print("读取原始数据：");
type(data)
print(data);
data_zs = 1.0*(data - data.mean())/data.std() #数据标准化 使用规范化方法       https://blog.csdn.net/bbbeoy/article/details/70185798
print("========data-zs========")
print(data_zs)
print("》》》》》》========data-zs========over《《《《《")
from sklearn.cluster import KMeans
model = KMeans(n_clusters = k, n_jobs = 4, max_iter = iteration) #分为k类，并发数4
model.fit(data_zs) #开始聚类
#简单打印结果
r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心
r = pd.concat([r2, r1], axis = 1) #横向连接（axis=0是纵向），得到聚类中心对应的类别下的数目
r.columns = list(data.columns) + [u'类别个数'] #重命名表头
print("=====>>>>>>>>>r<<<<<<<<<===")
print(r)
print("=====>>>>>>>>>r over!!!!!<<<<<<<<<===")
print(data)
print("========model.labelss_=========")
print(pd.Series(model.labels_, index = data.index))
#详细输出原始数据及其类别
r = pd.concat([data, pd.Series(model.labels_, index = data.index)], axis = 1)  #详细输出每个样本对应的类别
r.columns = list(data.columns) + [u'聚类后类别'] #重命名表头
print(r)
#r.to_excel(outputfile) #保存结果
# matplotlib 可视化显示
predict = model.predict(data_zs);#一定要传入预处理过的数集data_zs，不能位原始数据data
# 输出的都是聚类类别
print(predict)
# matplotlib 可视化显示
plt.figure(figsize=(5, 5));
colored = ["orange", "green", "blue"];
colr = [colored[i] for i in predict];
plt.scatter(data_zs.values[:,0], data_zs.values[:,1], color=colr);#将DataFrame对象X_df转成ndarray数组即可,https://blog.csdn.net/m0_38052384/article/details/103161009
plt.show();