# -*- coding: utf-8 -*-

# @File    : scipy_demo.py
# @Date    :  2019-11-24 18:00
# @Author  : admin
from scipy import signal,misc
import matplotlib.pyplot as plt
import numpy as np
image=misc.ascent() #二维图像，公寓图像
w=np.zeros((50,50))
w[0][0]=1.0 #修改参数调整滤波器
w[49][25]=1.0 #可以根据需要调整
image_new=signal.fftconvolve(image,w) #使用FFT算法进行卷积

plt.figure()
plt.imshow(image_new) #显示滤波后的图像
plt.gray()
plt.title("Filteres image!")
plt.show()