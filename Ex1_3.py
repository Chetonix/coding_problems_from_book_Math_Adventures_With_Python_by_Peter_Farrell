from turtle import *

wn = Screen()
shape("turtle")
speed(0)

def triangle(sidelength = 100):
    for _ in range(3):
        forward(sidelength)
        left(360/3)

triangle()
wn.exitonclick()