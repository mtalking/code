# coding=utf-8

from turtle import *

#定义绘制弧形的函数curvemove
def curvemove(step):
    for i in range(step):
        right(1)
        forward(1)

#设置绘图标志的形状
shape("turtle")
#设置绘图速度
speed(10)      

#绘制字母I
#设置颜色，第一个参数为线形颜色，第二个参数为填充颜色
color("gray","pink")
up()
#从点（-300，120）开始绘图
goto(-300,120)
#设置线条宽度
pensize(10)
down()
#设置每一步的步长和角度
forward(100)
backward(50)
right(90)
forward(200)
right(90)
forward(50)
backward(100)

#绘制字母U
#设置颜色
color("gray","pink")
up()
#从点（300，120）开始绘图
goto(300,120)
down()
#设置每一步的步长和角度
left(90)
forward(150)
curvemove(180)
forward(149)

#绘制心形
#设置线条宽度
pensize(5)
#设置颜色
color("red","pink") 
up()
#从点（-30，-80）开始绘图
goto(-30,-80)
down()
#颜色填充开始
begin_fill()
#设置每一步的步长和角度
left(35)
forward(111.65)
curvemove(200)
left(120)
curvemove(200)
forward(111.65)
#颜色填充开始
end_fill()


#设置绘图标记的结束位置
up()
goto(-300,-120)

#绘图结束
done()
