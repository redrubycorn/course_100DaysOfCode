# date: 09-July-2024

# turtle docs
# https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen

my_turtle = Turtle()
print(my_turtle)
my_turtle.shape("turtle")
my_turtle.color("coral")

my_turtle.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()