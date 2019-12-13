# -*- coding: utf-8 -*-

# @File    : figure_demo3.py
# @Date    :  2019-11-24 17:33
# @Author  : admin
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
# scatter散点图
X = np.linspace(1, 10, 100)
Y = np.sin(X)
ax1.scatter(X, Y)
ax1.set_title("Y=sin(X)")
#直方图
X1 = np.random.randn(100)
ax2.hist(X1,normed=True,bins=3)
ax2.set_title("Hist")
#折线图
X2 = np.linspace(1, 10, 4)
Y2 = np.sin(X2)
ax3.plot(X2,Y2)
#箱线图-小提琴图-四分位数的统计
# ax4.boxplot(X1,whis=0.5,sym="^")
X=[0.4,0.1,0.1,0.4]
labels=["A","B","C","D"]
ax4.pie(X,labels=labels,shadow=True,explode=[0.3,0,0,0.5])

plt.show()