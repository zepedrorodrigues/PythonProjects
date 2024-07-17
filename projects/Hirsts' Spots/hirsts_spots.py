import random
from random import choice
import colorgram
from colorgram import extract
import turtle
from turtle import Turtle

turtle.colormode(255)

rgb_colours = []
colours = colorgram.extract(r"C:\Users\jpnms\Desktop\hirsts_spots.jpeg",30)
for colour in colours:
    r= colour.rgb.r ; g = colour.rgb.g ; b = colour.rgb.b
    rgb_colours.append((r,g,b))

timmy = Turtle()
timmy.speed(0)

timmy.pu()
timmy.right(135)
timmy.forward(300)
timmy.left(135)
for x in range(10):
    for x in range(10):
        timmy.dot(20,random.choice(rgb_colours))
        timmy.forward(50)
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.left(180)

screen = turtle.Screen()
screen.exitonclick()