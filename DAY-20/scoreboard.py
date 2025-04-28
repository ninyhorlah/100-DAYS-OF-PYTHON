from turtle import Turtle

turtle = Turtle()
ALIGNMENT =  "center"
FONT = ("Arial", 24, "normal")

    

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../../../../Desktop/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} Highest Score = {self.high_score}", align=ALIGNMENT , font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT , font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../Desktop/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    # def highest_score(self):
    #     pass
