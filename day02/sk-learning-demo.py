# -*- coding: utf-8 -*-

# @File    : sk-learning-demo.py
# @Date    :  2019-12-12 21:53
# @Author  : admin
from sklearn.feature_extraction import  DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
dic={"city":"北京","age":1000};
list=[{"city":"北京","age":1000},{"city":"天津","age":800}];
print(list)
def dictVec():
    dict=DictVectorizer(sparse=False);
    data=dict.fit_transform(list);
    print(dict.get_feature_names())
    print(data);
    return None;
def dictVecText():
    cv=CountVectorizer();
    data=cv.fit_transform(["life is short,but i love"," python,python is easy language"])
    print(cv.get_feature_names())
    print(data.toarray())
    return None
dictVec()
dictVecText();
