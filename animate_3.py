from turtle import Screen, update, clear, forward, penup, pendown
from parts import draw_triangle
from helpers import setup
import settings
import time

def draw_animation(num_frames, sidelen, color, sleeptime):
    for i in range(num_frames):
        if i < num_frames // 2:
            forward(1)

        elif i > num_frames // 2:
            penup()
            forward(-1)
            pendown()

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