# -*- coding: utf-8 -*-

# @File    : oop_print_demo.py
# @Date    :  2019-11-24 17:53
# @Author  : admin
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)
X=np.linspace(-10,10,100)
Y1=np.sin(X)
Y2=np.tanh(X)
Y3=np.sign(X)
ax1.plot(X,Y1,"r--")
ax1.set_title("Y=SIN(X)")
ax1.set_xlabel("X")
ax1.set_ylabel("Y1")

ax2.plot(X,Y2,color="b",linestyle="-.",linewidth=2)
ax2.set_title("Y=tanh(X)")
ax2.set_xlabel("X")
ax2.set_ylabel("Y2")
ax2.legend(labels=["Y=tanh(X)"])

ax3.plot(X,Y3,"g-",marker="o")
ax3.set_title("Y=sign(X)")
ax3.set_xlabel("X")
ax3.set_ylabel("Y3")

plt.show()