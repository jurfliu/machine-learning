from matplotlib import pyplot as plt
x=range(2,26,2);
y=[15,13,14,5,17,20,25,26,27,22,18,15];
print([x for x in y])
#设置图片的大小,dpi为分辨率
plt.figure(figsize=(20,8),dpi=50);
#设置x,y轴的刻度，让其变稀疏或者稠密
x_label=[i/2 for i in range(4,49)]
plt.xticks(x_label[::2])  #[]
plt.yticks(range(min(y),max(y)+1))


#绘图
plt.plot(x,y)

#保存
plt.savefig("./t1.png");
#显示
plt.show();