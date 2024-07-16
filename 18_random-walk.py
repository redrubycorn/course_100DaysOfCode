# turtle documentation
# https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen
import random

robot = Turtle()
robot.pensize(20)
robot.speed("fastest")

colors = ["lightcoral", "firebrick", "olive", "dodgerblue", "crimson", "darkblue", "royalblue", "mediumvioletred", "hotpink", "green", "gold"]
directions = [0, 90, 180, 270]

for _ in range(100):
    robot.color(random.choice(colors))
    robot.forward(40)
    robot.setheading(random.choice(directions))

# should be at the bottom of the document
screen = Screen()
screen.exitonclick()