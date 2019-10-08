from turtle import *
t=Turtle()
w=Screen()
w.bgcolor("black")
l=["blue","red","orange","yellow","green"]
for i in range(5):
    t.pencolor(l[i])
    t.pensize(6)
    t.circle(80)
    t.left(360)
    t.pensize(6)
    t.penup()
    t.forward(100)
    t.pendown()




done()



