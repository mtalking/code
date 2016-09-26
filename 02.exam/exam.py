# coding=utf-8

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#读取csv数据
data = pd.read_csv('exam.csv')

data_unbalanced = pd.read_csv('exam_unbalanced.csv')




#画出分布曲线
fig = plt.figure('balanced vs unbalanced')
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
#设置横坐标
ax1.set_xlabel(' balanced sample ')
ax2.set_xlabel(' unbalanced sample ')

#分别绘图
ax1.plot(data[data.y_label==1].x1,data[data.y_label==1].x2,'yo',label='negative', linewidth=2)
ax1.plot(data[data.y_label==0].x1,data[data.y_label==0].x2,'mD',label='positive', linewidth=2)
ax1.axis([20,100,30,100])


ax2.plot(data_unbalanced[data_unbalanced.y_label==1].x1,data_unbalanced[data_unbalanced.y_label==1].x2,'yo',label='negative', linewidth=2)
ax2.plot(data_unbalanced[data_unbalanced.y_label==0].x1,data_unbalanced[data_unbalanced.y_label==0].x2,'mD',label='positive', linewidth=2)
ax2.axis([20,100,30,100])
ax2.legend(loc='upper right')

plt.show()




