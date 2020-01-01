from matplotlib.font_manager import FontManager, FontProperties
from matplotlib import pyplot as plt, font_manager
from numpy import random
'''
背景：统计上午10-12点，气温的变化情况
'''
x=range(0,120);
y=[random.randint(20,35) for i in range(120)]
#设置字体的方式
#my_font=font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc");
#windows中的解决办法
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.figure(figsize=(20,8),dpi=60)
#调增x轴的稀疏

plt.plot(x,y)
x_labels=["10点{}分".format(i) for i in range(60)];
x_labels=x_labels+["11点{}分".format(i) for i in range(60)];
#取步长，数字和字符串一一对应，数据的长度一样 list(x),转成list，才能用切片，rotation 旋转的度数
plt.xticks(list(x)[::3],x_labels[::3],rotation=90)#
#添加描述信息
plt.xlabel("时间")
plt.ylabel("温度 单位(℃)")
plt.title("北京市10点到12点的温度化")

plt.show();