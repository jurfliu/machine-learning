# -*- coding: utf-8 -*-

# @File    : test.py
# @Date    :  2019-12-21 18:19
# @Author  : admin

import pandas as pd
from sklearn.decomposition import  PCA
products = pd.read_csv("../data/products.csv")
orders = pd.read_csv("../data/orders.csv")
aisles = pd.read_csv("../data/aisles.csv")
products=products.head(100);
print(products)