from turtle import *

t=Turtle()
l=["red","yellow","blue","green","orange"]
for i in range(5):
    t.pencolor(l[i])
    t.forward(300)
    t.left(216+i)
   # t.pensize(i)

done()