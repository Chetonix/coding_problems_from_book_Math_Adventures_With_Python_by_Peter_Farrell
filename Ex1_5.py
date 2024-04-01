from turtle import *

wn = Screen()
shape("turtle")
speed(0)

l = 5

def square(length=100):
    for _ in range(4):
        forward(length)
        left(90)

for _ in range(72):
    square(l)
    left(5)
    l += 5
    square(l)


wn.exitonclick()