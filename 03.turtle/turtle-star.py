# coding=utf-8

import turtle
from turtle import *
import time


#定义绘制时画笔的形状为"turtle"
shape("turtle")
#定义线条颜色为红色，填充颜色为黄色
color("red","yellow")
#填充开始
begin_fill()
#定义绘制时画笔的线条宽度为5
pensize(5)
#定义绘图的速度为5
speed(5)
#以0,0为起点进行绘制
goto(0,0)

#循环5次绘出五角星的五条边
#每次循环向前移动200步，向右移动144°
for i in range(5):
    forward(200)
    right(144)
#填充结束
end_fill()

#将画笔移动到点（-150，-120），移动时不绘图
up()
goto(-150,-120)

#设置绘图结束后的画笔颜色
color("yellow")

#绘图结束
done()





