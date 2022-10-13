# Helpers
# By Chris Proctor
# ----------------
# A mishmash of useful functions. Feel free to use these in your own projects if they are helpful to you.

from turtle import *

def setup(x, y):
    '''Sets up the turtle, ready to draw,
    at the given coordinates'''
    hideturtle()
    penup()
    goto(x,y)
    pendown()
    speed(0)
    setheading(0)
    tracer(0)


def update_position(x, y=None):
    """
    Updates the turtle's position, adding x to the turtle's current x and y to the
    turtle's current y. This may be called in two different ways:
        update_position(10, 20)
        update_position([10, 20])
    """
    if y is None:
        x, y = x
    current_x, current_y = position()
    penup()
    goto(x + current_x, y + current_y)
    pendown()

