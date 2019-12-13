# -*- coding: utf-8 -*-

# @File    : model_save.py
# @Date    :  2019-11-27 18:13
# @Author  : admin
'''
sklearn是一个Python第三方提供的非常强力的机器学习库，它包含了从数据预处理到训练模型的各个方面。
在实战使用scikit-learn中可以极大的节省我们编写代码的时间以及减少我们的代码量，使我们有更多的精力去分析数据分布，调整模型和修改超参
https://bigquant.com/community/t/topic/127078
https://blog.csdn.net/yuanshuaipeng/article/details/80399863
'''
from sklearn.datasets import load_iris
#导入数据集
iris=load_iris();
#数据切分
x=iris.data  #获得其特征向量
y=iris.target #获得样本label
print("特征性向量:",x);
print("特征性向量:",y);
#切分数据集
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=22)
#建立使用随机深林建立模型
from sklearn.ensemble import RandomForestClassifier
rmf=RandomForestClassifier(n_estimators=100)   #n_estimators:森林里（决策）树的数目
#训练模型
rmf.fit(x_train,y_train)
#预测
y_pred=rmf.predict(x_test)
#校验模型
print("model in train set score is:",rmf.score(x_train,y_train))
print("model in test set score is:",rmf.score(x_test,y_test))
#保存模型
#from sklearn.externals import joblib
import joblib
joblib.dump(rmf,"iris.pkl")