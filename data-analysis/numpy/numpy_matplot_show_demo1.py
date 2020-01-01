# -*- coding: utf-8 -*-

# @File    : numpy_matplot_show_demo1.py
# @Date    :  2020-01-01 10:22
# @Author  : admin
from matplotlib import pyplot as plt
import numpy as np
print("###########################################1.加载数据#################################")
us_file_path = "./US_video_data_numbers.csv"
t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=False);
print(t1)
#取评论的数据
h=t1[0:100];
print("=============================截取的行================")
print(h)
t_us_comments = h[:,-1];
print(t_us_comments);
#选择比5000小的数据
t_us_comments = t_us_comments[t_us_comments<=5000]
print(t_us_comments);
distance=50
#组数
y=(t_us_comments.max()-t_us_comments.min())//distance

#绘图
plt.figure(figsize=(20,8),dpi=80)

plt.hist(t_us_comments,y)


plt.show()

