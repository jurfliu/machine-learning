# -*- coding: utf-8 -*-

# @File    : sk-learn-jiangwei.py
# @Date    :  2019-12-21 13:47
# @Author  : admin
from sklearn.feature_selection import  VarianceThreshold
from  sklearn.decomposition import PCA
##特征选择-删除方差低的特征
def jiangwei():
     var=VarianceThreshold(threshold=0.0);
     data=var.fit_transform([[0,2,0,3],[0,1,4,3],[0,1,1,3]])
     print(data)
     return None;
'''
class PCA(sklearn.decomposition.base)
   """
   主成成分分析

   :param n_components: int, float, None or string
       这个参数可以帮我们指定希望PCA降维后的特征维度数目。最常用的做法是直接指定降维到的维度数目，此时n_components是一个大于1的整数。
       我们也可以用默认值，即不输入n_components，此时n_components=min(样本数，特征数)

   :param whiten: bool, optional (default False)
      判断是否进行白化。所谓白化，就是对降维后的数据的每个特征进行归一化。对于PCA降维本身来说一般不需要白化,如果你PCA降维后有后续的数据处理动作，可以考虑白化，默认值是False，即不进行白化

   :param svd_solver:
      选择一个合适的SVD算法来降维,一般来说，使用默认值就够了。
    """


'''
def pcademo():
    r=PCA(n_components=0.9);
    data=r.fit_transform([[2,8,4,5],[6,3,0,8],[5,4,9,1]])
    print(data)
    return None;

pcademo();
#jiangwei()
'''
[0,2,0,3],
[0,1,4,3],
[0,1,1,3]
第一列，第四列的方差均为0，所以舍弃
'''
