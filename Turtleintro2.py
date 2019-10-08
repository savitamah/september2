from turtle import *
t=Turtle()
w=Screen()
#w.bgcolor("Yellow")
#w.bgpic("school.gif")
w.title("My first turtle program")
t.shape("turtle")
t.pensize(10)
t.speed(6)
t.hideturtle()
#'fastest':0
#'fast':10
#'normal':6
#'slow':3
#'slowest':1
#t.shape("circle")
'''t.color("red","green")
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)'''
t.pencolor("Yellow")
t.fillcolor("red")
t.begin_fill()
for i in range(4):
    t.fd(100)
    t.left(90)
t.end_fill()
   # t.bk(500)



done()

