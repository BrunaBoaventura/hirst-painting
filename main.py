import turtle
import random

color_list = [(115, 160, 192), (134, 46, 112), (242, 243, 246), (103, 34, 79), (200, 121, 179), (163, 62, 43),
              (18, 25, 48), (122, 121, 127)]
turtle.colormode(255)
turtle.hideturtle()
turtle.penup()
turtle.goto(-230, -230)
turtle.speed("fastest")


def line_work():
    for space in range(10):
        turtle.dot(20, random.choice(color_list))
        turtle.forward(50)


def move_up():
    position = turtle.position()
    turtle.goto(-230, position[1] + 50)


for i in range(10):
    line_work()
    move_up()

screen = turtle.Screen()
screen.exitonclick()
