# -*- coding: utf-8 -*-

# @File    : numpy_pingjie_demo.py
# @Date    :  2020-01-01 9:49
# @Author  : admin
import numpy as np
t1=np.arange(0,6).reshape(2,3)
print(t1)
t2=np.arange(0,12).reshape(4,3)
print(t2)
#按垂直拼接
t3=np.vstack((t1,t2));
print(t3)
t5=np.arange(0,12).reshape(2,6)
#按水平拼接
t4=np.hstack((t1,t5));
print(t4)
#换行,第一行和第二行已经换行了
t1[[0,1],:]=t1[[1,0],:]
print(t1)
#换列，第一列和第二列
t1[:,[1,2]]=t1[:,[2,1]];
print(t1)

def  show():
    # 添加国家信息
    us_file_path = "./US_video_data_numbers.csv"
    us_content = np.loadtxt(us_file_path, delimiter=",", dtype="int");
    gb_file_path = "./GB_video_data_numbers.csv"
    gb_content = np.loadtxt(gb_file_path, delimiter=",", dtype="int");
    print(us_content);
    print("====================")
    print(gb_content);
    # 构造全为0的数据
    zeros_data = np.zeros((us_content.shape[0], 1)).astype(int)
    ones_data = np.ones((gb_content.shape[0], 1)).astype(int)
    print(zeros_data);
    print(ones_data)
    # 分别添加一列全为0,1的数组，水平拼接一列
    us_data = np.hstack((us_content, zeros_data))
    uk_data = np.hstack((gb_content, ones_data))
    # 拼接两组数据，垂直拼接
    final_data = np.vstack((us_data, uk_data))
    print(final_data)

show();


