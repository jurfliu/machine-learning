# -*- coding: utf-8 -*-

# @File    : numpy_fixempty_value_demo.py
# @Date    :  2019-12-31 17:28
# @Author  : admin
import numpy as np

print("##############################构造一个含有nan的矩阵")
t = np.arange(0,24).reshape(4,6)
#将元素转成float类型
t=t.astype(np.float)
print(t)
print("######################赋值为nan后")
#给某个位置赋值nan
t[[1,3],[2,4]]=np.nan;#(1,2),(3,4)
print(t);
print("##############################为含有nan的行赋值为均值")
#t.shape[0] 行，t.shape[1] 列
print(t.shape,t.shape[0],t.shape[1])
#开始遍历 np.count_nonzero(e!=e)
def method2():
  for i in range(t.shape[1]):
      temp_col=t[:,i];
      nan_num=np.count_nonzero(temp_col!=temp_col); #为nana的个数
      print(nan_num)
      if nan_num >0 :
          not_nan_col=temp_col[temp_col==temp_col];  #不为nan
          print(not_nan_col)
          temp_col[np.isnan(temp_col)]=not_nan_col.mean();#赋值

def method1():
  for i in range(t.shape[1]):
    print(t[:,i])
    nan_num = np.count_nonzero(t[:, i][t[:, i] != t[:, i]]);  # 计算为nan的个数 A[true,false,false]
    print(nan_num)
    if nan_num > 0:
        new_col = t[:, i];
        #这两步是重点
        new_col_not_nan = new_col[np.isnan(new_col) == False].sum();  # 不为nan的元素求和
        '''
        1
        nan
        1
        nan
        1
        1
        t.shape[[0] - nan_num   5-2
        '''
        new_col_means = new_col_not_nan / (t.shape[0] - nan_num);  # 和/个数
        new_col[np.isnan(new_col)] = new_col_means;  # 赋值为均值
        t[:, i] = new_col;  # 更新t的当前列




print("结果如下:")
method2();
print(t)



