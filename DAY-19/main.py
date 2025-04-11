from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)
user_guess = screen.textinput(title="what's your bet", prompt="Guess the winning turtle. Choose a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -70, -40, -10, 20, 50]
all_turtles = []

for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=-230, y=y_positions[turtle])
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:

    for turtles in all_turtles:
        if turtles.xcor() > 220:
            is_race_on = False
            winning_turtle = turtles.pencolor()
            if winning_turtle == user_guess:
                print(f"You've won!. The {winning_turtle} turtle is the winner.")
            else:
                print(f"You've lost!. The {winning_turtle} turtle is the winner.")
        random_pos = random.randint(0, 10)
        turtles.fd(random_pos)

screen.exitonclick()