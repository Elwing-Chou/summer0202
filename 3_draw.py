import turtle
import random

turtle.shape("turtle")
turtle.colormode(255)
turtle.speed(3)

radius = 150
turtle.penup()
turtle.forward(radius)
turtle.pendown()
turtle.left(90)

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
turtle.fillcolor(r,g,b)
turtle.begin_fill()
turtle.circle(radius, 180)
turtle.end_fill()

turtle.done()