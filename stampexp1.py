import turtle
import random
import time
screen=turtle.Screen()
trt1=turtle.Turtle()
screen.setup(420,32)
trt1.shape('turtle')
trt1.color('darkgoldenrod','black')
s=10
#trt1.penup()
#trt1.setpos(30,30)
for i in range(28):
        s=s+2
        trt1.stamp()
        trt1.forward(s)
        trt1.right(25)
        time.sleep(0.25)
