# -*- coding: utf-8 -*-

# @File    : matplot-zhexian-demo3.py
# @Date    :  2019-12-30 10:57
# @Author  : admin
from matplotlib import pyplot as plt
from matplotlib import font_manager
#windows中的解决办法
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_1 = [15746,312,4497,319]
b_2 = [12357,156,2045,168]
b_3 = [2358,399,2358,362]
bar_width=0.2  #设置柱状图的宽度
#设置x轴的刻度,难点注意 x_3比x_2比x_1 分别都多一个bar_width,这样才能，三条柱子紧邻在一起
x_1=list(range(len(a)))
x_2=[i+bar_width for i in x_1]
x_3=[i+bar_width*2 for i in x_1]

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)
plt.bar(x_1,b_1,width=bar_width,label="9月14日") #label可以在legend显示
plt.bar(x_2,b_2,width=bar_width,label="9月15日")
plt.bar(x_3,b_3,width=bar_width,label="9月16日")

#设置图例
plt.legend(loc="upper left")
#设置x轴的刻度
plt.xticks(x_1,a)
plt.show()
