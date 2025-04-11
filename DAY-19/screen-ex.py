from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def fd():
    tim.fd(10)

def bw():
    tim.bk(10)

def lt():
    tim.lt(10)

def rt():
    tim.rt(10)

def cl():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(fd, "w")
screen.onkey(bw, "s")
screen.onkey(lt, "a")
screen.onkey(rt, "d")
screen.onkey(cl, "c")


screen.listen()
screen.exitonclick()