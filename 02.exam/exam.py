# coding=utf-8

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#读取平衡数据集exam.csv，存入变量data
data = pd.read_csv('exam.csv')

#读取不平衡数据集exam_unbanlanced.csv，存入变量data_unbalanced
data_unbalanced = pd.read_csv('exam_unbalanced.csv')


#画图
#用两个子图分别展示平衡数据集和不平衡数据集
fig = plt.figure('balanced vs unbalanced')
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
#设置子图1的横坐标
ax1.set_xlabel(' balanced sample ')
#设置子图1的横坐标
ax2.set_xlabel(' unbalanced sample ')

#在子图1上绘制平衡数据集
ax1.plot(data[data.y_label==1].x1,data[data.y_label==1].x2,'yo', linewidth=2)
ax1.plot(data[data.y_label==0].x1,data[data.y_label==0].x2,'mD', linewidth=2)
ax1.axis([20,100,30,100])

#在子图2上绘制不平衡数据集
ax2.plot(data_unbalanced[data_unbalanced.y_label==1].x1,data_unbalanced[data_unbalanced.y_label==1].x2,'yo',label='negative', linewidth=2)
ax2.plot(data_unbalanced[data_unbalanced.y_label==0].x1,data_unbalanced[data_unbalanced.y_label==0].x2,'mD',label='positive', linewidth=2)
ax2.axis([20,100,30,100])
#在子图2上显示图例
ax2.legend(loc='upper right')


plt.show()




