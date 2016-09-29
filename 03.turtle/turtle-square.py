# coding=utf-8

import turtle

#绘出正方形的四条边
#循环4次，每次前进200步，再右转90度
for i in range(4):
    turtle.forward(200)
    turtle.right(90)

#绘图结束
turtle.done()