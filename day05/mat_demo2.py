# -*- coding: utf-8 -*-

# @File    : mat_demo2.py
# @Date    :  2019-11-24 17:17
# @Author  : admin
import matplotlib.pyplot as plt
import numpy as np
X=np.linspace(1,10)
y=5+X
#plot绘制直线图
plt.plot(X,y)
y1=5+2*X
plt.plot(X,y1)
plt.title(u"This is 函数 y=x",fontproperties="SimHei")
#x,y轴命名
plt.xlabel("X")
plt.ylabel("Y")
plt.show();