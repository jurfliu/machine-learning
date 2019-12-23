# -*- coding: utf-8 -*-

# @File    : kmeans_demos.py
# @Date    :  2019-12-22 12:14
# @Author  : admin
# -*- coding: utf-8 -*-

# @File    : sk-learn-classficify.py
# @Date    :  2019-12-21 16:15
# @Author  : admin
import pandas as pd
from sklearn.decomposition import  PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
'''
数据如下：

order_products__prior.csv：订单与商品信息

字段：order_id, product_id, add_to_cart_order, reordered
products.csv：商品信息

字段：product_id, product_name, aisle_id, department_id
orders.csv：用户的订单信息

字段：order_id,user_id,eval_set,order_number,….
aisles.csv：商品所属具体物品类别

字段： aisle_id, aisle
————————————————
版权声明：本文为CSDN博主「心灵在路上」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
https://blog.csdn.net/weixin_44513830/article/details/99937668
'''
def pcademo():
# 去读四张表的数据
  prior = pd.read_csv("../data/order_products__prior.csv")
  products = pd.read_csv("../data/products.csv")
  orders = pd.read_csv("../data/orders.csv")
  aisles = pd.read_csv("../data/aisles.csv")
#
  products=products.head(1000);
  orders=orders.head(1000);
# 合并四张表
  mt = pd.merge(prior, products, on=['product_id', 'product_id'])
  mt1 = pd.merge(mt, orders, on=['order_id', 'order_id'])
  mt2 = pd.merge(mt1, aisles, on=['aisle_id', 'aisle_id'])
# pd.crosstab 统计用户与物品之间的次数关系（统计次数）
  cross = pd.crosstab(mt2['user_id'], mt2['aisle'])
# PCA进行主成分分析
  pc = PCA(n_components=0.95)
  data = pc.fit_transform(cross)
  print(data);
  print(data.shape)
  print("==========聚类开始======")
  #预处理后的数据，抽取100个
  xdata=data[:200]
  km=KMeans(n_clusters=4)
  km.fit(xdata)
  predict=km.predict(xdata);
  #输出的都是聚类类别
  print("====predict====")
  print(predict)
  #matplotlib 可视化显示
  plt.figure(figsize=(5,5));
  colored=["orange","green","blue","yellow"];
  colr=[colored[i] for i in predict];
  plt.scatter(xdata[:,1],xdata[:,10],color=colr);
  plt.show();

pcademo();