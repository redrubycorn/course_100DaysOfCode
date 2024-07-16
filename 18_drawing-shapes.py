# turtle documentation
# https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen
import random

tommy = Turtle()
tommy.shape("turtle")

colors = ["lightcoral", "firebrick", "olive", "dodgerblue", "crimson", "darkblue", "royalblue", "mediumvioletred", "hotpink", "green", "gold"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tommy.forward(100)
        tommy.right(angle)

for num_sides in range(3, 11):
    tommy.color(random.choice(colors))
    draw_shape(num_sides)


# should be at the bottom of the document
screen = Screen()
screen.exitonclick()