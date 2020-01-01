#!usr/bin/env python
#-*- coding:utf-8 _*-
'''
@author:Administrator
@file: matplot-zhuzhuang-demo.py
@time: 2019-12-29 下午 5:52
'''
from matplotlib import  pyplot as plt

a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士","摔跤吧！爸爸","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]

b=[56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]
#windows下设置字体
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#设置图形大小
plt.figure(figsize=(10,5),dpi=80)
#绘制条形图
plt.bar(range(len(a)),b,width=0.3);
#设置字符串到x轴,x轴的标签与x轴的数据绑定
plt.xticks(range(len(a)),a,rotation=90)

plt.savefig("./movie.png")

plt.show()

