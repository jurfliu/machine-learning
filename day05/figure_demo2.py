# -*- coding: utf-8 -*-

# @File    : figure_demo2.py
# @Date    :  2019-11-24 17:29
# @Author  : admin
import matplotlib.pyplot as plt
fig=plt.figure()
ax1=fig.add_subplot(221)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(224)
#面向对象的写法
import  numpy as np
X = np.arange(10)
ax1.plot(X,X)
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_title("Y=X")
ax2.plot(X,-X)
ax3.plot(-X,X)
ax4.plot(-X,-X)
plt.show()