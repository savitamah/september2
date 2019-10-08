from turtle import *

t = Turtle()
w = Screen()
for i in range(15):
 t.begin_fill()
 t.pencolor("red")
 t.fillcolor("pink")
 t.pensize(3)
 t.left(90)
 t.forward(300)
 t.left(60)
 t.end_fill()
done();
