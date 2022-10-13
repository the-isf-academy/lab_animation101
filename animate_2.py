from turtle import Screen, clear, update
from parts import customized_circle
from helpers import setup
import settings
import time

def draw_animation(num_frames, radius, speedfactor, color, sleeptime):
    circle_size = radius

    for i in range(num_frames//2):
        circle_size = circle_size + speedfactor
        customized_circle(circle_size, color)

        update()
        time.sleep(sleeptime)
        clear()


    for j in range(num_frames//2):
        circle_size = circle_size - speedfactor
        customized_circle(circle_size, color)

        update()
        time.sleep(sleeptime)
        clear()


def main():
    screen = Screen()
    screen.setup(settings.SCREENWIDTH,settings.SCREENHEIGHT)
    
    for i in range(settings.NUMREPEATS):
        setup(settings.START_X,settings.START_Y)
        draw_animation(settings.NUMFRAMES, settings.RADIUS, settings.SPEEDFACTOR, settings.COLOR, settings.SLEEPTIME)

main()