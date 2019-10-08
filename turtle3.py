from turtle import *

t=Turtle()
l=["red","yellow","blue","green","orange"]
t.circle(50)
t.circle(-50)
#t.reset()
t.undo()
t.forward(100)
t.circle(100,steps=10)
t.bk(200)
t.circle(100,180)
#t.goto(-50,-50)
t.stamp()
done()