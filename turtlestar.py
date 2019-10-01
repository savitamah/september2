from turtle import *

t=Turtle()
l=["red","yellow","blue","green","orange"]
for i in range(55):
    t.pencolor(l[i%5])
    t.forward(200)
    t.left(216+i)
    # t.pensize(i)

done()