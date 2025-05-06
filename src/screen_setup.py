import turtle

import config
from turtle import Screen, Turtle

def screen_setup():
    screen = Screen()
    screen.setup(width=config.SCREEN_WIDTH, height=config.SCREEN_HEIGHT)
    screen.tracer(0)  # Turns animation off so that we can refresh the screen with the desired rhythm
    screen.bgcolor('pink')
    screen.title('Turtle Crossing Game')
    return screen

def draw_line(vertical_or_horizontal: str, coordinate: int):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.up()

    # Drawing a vertical line at the x abscissa
    if vertical_or_horizontal == "vertical":
        turtle.goto(x=coordinate, y=-config.SCREEN_HEIGHT/2)
        turtle.down()
        turtle.goto(x=coordinate, y=config.SCREEN_HEIGHT/2)
        turtle.write(coordinate)

    # Drawing a vertical line at the x abscissa
    elif vertical_or_horizontal == "horizontal":
        turtle.goto(x=-config.SCREEN_WIDTH/2, y=coordinate)
        turtle.down()
        turtle.goto(x=config.SCREEN_WIDTH/2, y=coordinate)
        turtle.write(coordinate)


def draw_grid(step: int):
    if config.SCREEN_HEIGHT % 10 != 0 or config.SCREEN_WIDTH % 10 != 0:
        raise ValueError("draw_grid() error: the grid's height and width must be multiples of 10")

    turtle = Turtle()
    turtle.hideturtle()
    turtle.up() # No writing at first
    turtle.goto(x=int(-config.SCREEN_WIDTH/2),y=int(-config.SCREEN_HEIGHT/2)) # Going to the initial position

    # Drawing vertical lines
    for i in range(int(-config.SCREEN_WIDTH/2),int(config.SCREEN_WIDTH/2)+step,step):
        turtle.up()
        turtle.goto(x=i,y=-config.SCREEN_HEIGHT/2)
        turtle.down()
        # Making the line bold when x = 0
        if i == 0:
            turtle.width(2)
        else:
            turtle.width(1)
        turtle.goto(x=i,y=config.SCREEN_HEIGHT/2)

    # Drawing horizontal lines for debugging purposes
    for i in range(int(-config.SCREEN_HEIGHT/2),int(config.SCREEN_HEIGHT/2)+step,step):
        turtle.up()
        turtle.goto(x=-config.SCREEN_WIDTH/2,y=i)
        turtle.down()
        # Making the line bold when y = 0
        if i == 0:
            turtle.width(2)
        else:
            turtle.width(1)
        turtle.goto(x=config.SCREEN_WIDTH/2,y=i)
