from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snakes()
        self.head = self.snakes[0]
    
    def create_snakes(self):
        for position in POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        new_snake = Turtle("square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def reset(self):
        for snake in self.snakes:
            snake.goto(1000,1000)
        self.snakes.clear()
        self.create_snakes()
        self.head = self.snakes[0]

    def extend(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for sna in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[sna - 1].xcor()
            new_y = self.snakes[sna - 1].ycor()

            self.snakes[sna].goto(new_x, new_y)


        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
