from turtle import Turtle, Screen
import random

tim = Turtle()
tim_screen = Screen()

colour = [(235, 234, 231), (234, 229, 232), (236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35)]


tim_screen.colormode(255)
tim.penup()
tim.speed(0)
tim.hideturtle()
tim.setheading(225)
tim.fd(300)
tim.setheading(0)

dots = 100
for dot in range(1, dots + 1):
    tim.dot(20, random.choice(colour))
    tim.fd(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)


tim_screen.exitonclick()