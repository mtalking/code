# coding=utf-8

import numpy as np
import pandas as pd 
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.cross_validation import train_test_split
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

#读取csv数据
data = pd.read_csv('german.csv')

#将标签赋值为变量y
y = data.y

#将坏客户的标签改为0
y[y==2]=0

#从data中删除y列，将样本存入变量X
X = data.drop(['y'],axis=1)

#查看样本及特征量
print "样本X及标签y维度："
print X.shape,y.shape
print 

#查看样本前5行示例
print "样本示例："
print X.head()
print 

#查看特征描述性统计
print "特征描述性统计:"
print X.describe().T 
print 

#查看好坏客户数量
print "好坏客户数量（1：好客户，0：坏客户）"
print y.value_counts()
print 

#划分训练样本、训练标签、测试样本、测试标签
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.33, random_state=42)
print "训练集、测试集样本维度："
print train_x.shape,test_x.shape
print 

#使用train_x train_y 训练逻辑回归模型
clf = LogisticRegression()
clf.fit(train_x,train_y)

#使用训练的模型预测test_x
proba = clf.predict_proba(test_x)
print "预测测试集样本违约概率（每行代表一个样本，第一列为该样本是坏客户的概率，第二列为该样本是好客户的概率）："
print proba
print 

#计算auc值
fpr, tpr, thresholds = roc_curve(test_y, proba[:, 1])
roc_auc = auc(fpr, tpr)
print "auc值：",roc_auc
print 

#画出ROC曲线
plt.plot(fpr, tpr,lw=1,label='ROC (area = %0.2f)' % (roc_auc))
plt.legend(loc='lower right')
plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')

plt.show()

#输入新客户的样本值，预测新客户的违约概率
proba = clf.predict_proba([1,24,2,26,2,3,2,1,4,26,1,1,2,1,2,1,0,1,1,0,1,0,1,0])
print "新客户预测："
print proba



