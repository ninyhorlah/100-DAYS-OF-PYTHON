from turtle import Turtle, Screen

screen = Screen()

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.fillcolor("white")
        self.goto(position)
        self.shapesize(stretch_len=1, stretch_wid=5)

    def go_up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def go_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)




    
