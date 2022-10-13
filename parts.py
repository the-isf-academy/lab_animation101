from turtle import color, begin_fill, forward, right, end_fill, circle

def draw_triangle(side_len, color_name):
    #This function draws an equilateral triangle
 
    color(color_name)
    begin_fill()
    for i in range(3):
        forward(side_len)
        right(120)
    end_fill()

def customized_circle(size, color_name):
    #This function draws a circle of a custom size and color 

    color(color_name)
    begin_fill()
    circle(size)
    end_fill()
