from turtle import *

wn = Screen()
shape("turtle")
speed(0)
def square(length):
    for _ in range(4):
        forward(length)
        left(90)

for _ in range(72):
    square(100)
    left(5)

wn.exitonclick()