# -*- coding: utf-8 -*-

# @File    : pca_demo.py
# @Date    :  2019-11-24 16:30
# @Author  : admin
import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
print(X.shape)
pca = PCA(n_components=2)  #n_components：这个参数可以帮我们指定希望PCA降维后的特征维度数目
pca.fit(X)#表示用数据X来训练PCA模型。
print("降维后各主成分方向：\n",pca.components_);
print("降维后各主成分的方差值：\n",pca.explained_variance_)  # doctest: +ELLIPSIS
print("降维后各主成分的方差值与总方差之比：\n",pca.explained_variance_ratio_)  # doctest: +ELLIPSIS
print("奇异值分解后得到的特征值：\n",pca.singular_values_)
print("降维后主成分数：\n",pca.n_components_)
    # [ 0.99244...  0.00755...]
print(pca.singular_values_)  # doctest: +ELLIPSIS
#https://www.cnblogs.com/eczhou/p/5433856.html