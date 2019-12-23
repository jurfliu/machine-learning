# -*- coding: utf-8 -*-

# @File    : k-2.py
# @Date    :  2019-12-18 23:26
# @Author  : admin
import pandas as pd
from sklearn.cluster import KMeans
def programmer_4():
    inputfile = 'e:/zscoreddata.xls'
    k = 5
    data = pd.read_excel(inputfile)

    kmodel = KMeans(n_clusters=k, n_jobs=4)
    kmodel.fit(data)

    print(kmodel.cluster_centers_)  # 查看聚类中心
    print("================")
    print(kmodel.labels_)  # 查看各样本对应的类别
    r1 = pd.Series(kmodel.labels_).value_counts()  # 统计各个类别的数目
    print("============r1====")
    print(r1)
    print(">>>>============r1====")
    r2 = pd.DataFrame(kmodel.cluster_centers_)  # 找出聚类中心
    r = pd.concat([r2, r1], axis=1)  # 横向连接（axis=0是纵向），得到聚类中心对应的类别下的数目
    r.columns = list(data.columns) + [u'类别个数']  # 重命名表头
    print(r)
programmer_4();