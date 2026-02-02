# 迴圈(不要改): 1. 次數在<後 2. i=0...9
# 開始: i = 0
# 條件: i < 10
# 增加: i = i + 1
i = 0
while i < 10:
    print(10-i)
    i = i + 1

# !!!!
import turtle
import random
turtle.shape("turtle")
turtle.speed(10)
turtle.colormode(255)

x = 100
total = 180 * (x - 2)
angle = total / x
i = 0
while i < x:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    turtle.pencolor(r, g, b)
    turtle.forward(10)
    turtle.left(180 - angle)
    i = i + 1

turtle.done()