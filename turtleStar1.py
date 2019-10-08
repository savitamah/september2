from turtle import *
t=Turtle()
l=["red","yellow","blue","green","orange"]
for i in range (55):
    t.pencolor(l[i%5])
    t.fd(100)
    t.left(216+i)
    t.pensize(i)
done()