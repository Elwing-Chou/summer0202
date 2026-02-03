import turtle
import random

turtle.shape("turtle")
turtle.colormode(255)
turtle.speed(0)

radius = 150
turtle.penup()
turtle.forward(radius)
turtle.pendown()
turtle.left(90)

i = 0
while i < 100:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    turtle.fillcolor(r,g,b)
    turtle.begin_fill()
    turtle.circle(radius-1*i, 180)
    turtle.end_fill()
    i = i + 1

turtle.done()