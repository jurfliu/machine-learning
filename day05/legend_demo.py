# -*- coding: utf-8 -*-

# @File    : legend_demo.py
# @Date    :  2019-11-24 17:48
# @Author  : admin
import numpy as np
import matplotlib.pyplot as plt
X=np.linspace(1,10,1000)
y1=X
plt.plot(X,y1,"r--",marker="o")
y2=X**2
plt.plot(X,y2,color="red",linestyle="--",linewidth=10)
y3=X**3
plt.plot(X,y3)
#使用loc=0默认是“best”,1-4分别是不同位置，ncol是列
plt.legend(labels=["Y=x","Y=X**2","Y=X**3"],loc="best",ncol=1)

plt.show()