from turtle import *

wn = Screen()
shape("turtle")
speed(0)

l = 5

def star(length=100):
    for _ in range(5):
        forward(length)
        right(144)

def starSpiral(l):
    for _ in range(360):
        star(l)
        right(5)
        l += 5
        star(l)

starSpiral(l)
wn.exitonclick()