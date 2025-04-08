from turtle import Turtle, Screen
import random
import colorgram

timmy_turtle = Turtle()
timmy_turtle_screen = Screen()

timmy_turtle.shape("turtle")

colors = colorgram.extract(
    "/Users/N.Akande/Desktop/tutorials/100-DAYS-OF-PYTHON/DAY-18/hierst-painting/image1.jpg",
    20,
)
rgb = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_rgb = (r, g, b)
    rgb.append(new_rgb)
# timmy_turtle.forward(100)
# timmy_turtle.right(90)
# timmy_turtle.forward(100)
# timmy_turtle.right(90)
# timmy_turtle.forward(100)
# timmy_turtle.right(90)
# timmy_turtle.forward(100)

# for _ in range(0, 10):
#     timmy_turtle.forward(15)
#     timmy_turtle.penup()
#     timmy_turtle.forward(15)
#     timmy_turtle.pendown()
#     # timmy_turtle.forward(15)

# shape_size = [3, 4, 5, 6, 7, 8, 9]
# shape_color = ["blue", "pink", "red", "grey", "purple", "aqua", "green"]

# for i in shape_size:
#     timmy_turtle.pencolor(shape_color[i - 3])
#     timmy_turtle.pencolor()
#     for size in range(1, i+1):
#         timmy_turtle.forward(120)
#         timmy_turtle.setheading(-(size * (360 / i)))

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_colour = (r, g, b)
    return rand_colour

# direction = [0, 90, 180, 270]
# timmy_turtle.pensize(15)
timmy_turtle.speed(0)


# for _ in range(200):
#     timmy_turtle_screen.colormode(255)
#     timmy_turtle.color(random_colour())
#     timmy_turtle.fd(30)
#     timmy_turtle.seth(random.choice(direction))

def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy_turtle_screen.colormode(255)
        timmy_turtle.color(random_colour())
        timmy_turtle.circle(100)
        timmy_turtle.left(size_of_gap)

spirograph(5)

timmy_turtle_screen.exitonclick()