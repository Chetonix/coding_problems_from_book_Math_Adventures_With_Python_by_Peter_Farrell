from turtle import *

wn = Screen()
shape("turtle")
speed(0)

def polygon(sidelength = 100, n = 3):
    for _ in range(n):
        forward(sidelength)
        left(360/n)

polygon(10, 120)
wn.exitonclick()