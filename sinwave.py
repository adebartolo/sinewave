import math
import turtle
# create screen with attributes
wn = turtle.Screen()
wn.setworldcoordinates(0,-1,1000,1)
wn.bgcolor('lightblue')

fred = turtle.Turtle()
fran = turtle.Turtle()

# Move Fran a specified amount to the right
turtle.forward(900)


# Code for Sin Wave
for x in range(720):
    y = math.sin(math.radians(x))
    fred.goto(x,y)

wn.exitonclick()
