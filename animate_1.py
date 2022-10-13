from turtle import  Screen, clear, update
from parts import draw_triangle
from helpers import update_position, setup
import settings
import time

def draw_animation(num_frames, sidelen, color, sleeptime):
    for i in range(num_frames):
        if i == num_frames/4:
            draw_triangle(sidelen, color)

        elif i == num_frames/2:
            update_position(100, 0)
            draw_triangle(sidelen, color)

        elif i == 3*(num_frames/4):
            update_position(200, 0)
            draw_triangle(sidelen, color)

        elif i == num_frames:
            update_position(100, 0)
            draw_triangle(sidelen, color)

        update()
        time.sleep(sleeptime)
    clear()
    

def main():
    screen = Screen()
    screen.setup(settings.SCREENWIDTH,settings.SCREENHEIGHT)

    for i in range(settings.NUMREPEATS):
        setup(settings.START_X,settings.START_Y)
        draw_animation(settings.NUMFRAMES, settings.SIDELEN, settings.COLOR, settings.SLEEPTIME)

main()