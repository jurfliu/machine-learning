# -*- coding: utf-8 -*-

# @File    : sk-learning-demo.py
# @Date    :  2019-12-12 21:53
# @Author  : admin
from sklearn.feature_extraction import  DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import jieba
dic={"city":"北京","age":1000};
list2=[{"city":"北京","age":1000},{"city":"天津","age":800}];
#print(list);
#字典的特征抽取
def dictVec():
    dict=DictVectorizer(sparse=False);
    data=dict.fit_transform(list2);
    print(dict.get_feature_names())
    print(data);
    return None;
#文本的特征提取
def dictVecText():
    cv=CountVectorizer();
    data=cv.fit_transform(["life is short,but i love  python","python is easy language"])
    print(cv.get_feature_names())
    print(data.toarray())
    return None
def  splitWords2():
    content1="Python是一种跨平台的计算机程序设计语言。是一种面向对象的动态类型语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发";
    content2="Python在设计上坚持了清晰划一的风格，这使得Python成为一门易读、易维护，并且被大量用户所欢迎的、用途广泛的语言。";
    #分词
    cuts1=jieba.cut(content1);
    cuts2=jieba.cut(content2);
    print(cuts1)
    #转成列表
    cList01=list(cuts1);
    cList02=list(cuts2);
    #转成字符串
    str1=" ".join(cList01);
    str2=" ".join(cList02);
    return str1,str2;
def  chineseTextVec2():
    cv=CountVectorizer();
    c1,c2=splitWords2();
    data=cv.fit_transform([c1,c2])
    print(cv.get_feature_names())
    print(data.toarray())
def  tfidfTextVec2():
    tf=TfidfVectorizer();
    c1,c2=splitWords2();
    data=tf.fit_transform([c1,c2])
    print(tf.get_feature_names())
    print(data.toarray())
#调用文本的特征提取
#dictVecText();
#字典的特征抽取
#dictVec()
#调用中文文本特征抽取
#chineseTextVec2();
tfidfTextVec2()
