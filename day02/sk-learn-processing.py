# -*- coding: utf-8 -*-

# @File    : sk-learn-processing.py
# @Date    :  2019-12-21 10:51
# @Author  : admin
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
#from sklearn.preprocessing import Imputer  0.22版本没有此函数
from sklearn.impute import SimpleImputer
import numpy as np
import numpy as np
list1=[90,2,10,40];
list2=[60,4,15,45];
list3=[75,3,13,46];
list=[];
list.append(list1)
list.append(list2)
list.append(list3)
#print(list)
def guiyihua():
    mm=MinMaxScaler();#默认归一化区间为0,1
    data=mm.fit_transform(list);
    print(data);
    return None;

def standDeal():
    X_train = np.array([[1., -1., 2.], [2., 0., 0.], [0., 1., -1.]])
    std = StandardScaler()
    X_train_std = std.fit_transform(X_train)
    print(X_train_std)
def fitempty():
     train_X = np.array([[1, 2], [np.nan, 3], [7, 6]])
     #imp = SimpleImputer(missing_values=np.nan, strategy='mean', axis=0)
     imp = SimpleImputer(missing_values=np.nan, strategy='mean')
     print(imp.fit(train_X));
     data=imp.fit_transform(train_X);
     print(data);
     return None;

#guiyihua();
#standDeal();
fitempty();