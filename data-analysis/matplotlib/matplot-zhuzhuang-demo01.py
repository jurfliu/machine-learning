#!usr/bin/env python
#-*- coding:utf-8 _*-
'''
@author:Administrator
@file: matplot-zhuzhuang-demo01.py
@time: 2019-12-29 下午 6:04
'''
from matplotlib import  pyplot as plt

a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士","摔跤吧！爸爸","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]

b=[56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]
#windows下设置字体
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#设置图形大小
plt.figure(figsize=(20,9),dpi=80)
#绘制条形图,注意barh（x,x,height=x），yticks两个函数的使用
plt.barh(range(len(a)),b,height=0.3);
#设置字符串到x轴,x轴的标签与x轴的数据绑定
#plt.xticks(range(len(a)),a,rotation=90)
plt.yticks(range(len(a)),a)

#plt.savefig("./movie.png")

plt.grid(alpha=0.3)
plt.show()
