import turtle
up_arrow = 'up'
left_arrow = 'left'
down_arrow = 'down'
right_Arrow = 'right'
spacebar = 'space'


UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP



def up():
    global direction
    direction = UP
    print('up')


def down():
    global direction
    direction = DOWN
    print('down')

def left():
    global direction
    direction = LEFT
    print('left')

def right():
    global direction
    direction = RIGHT
    print('right')
    
turtle.onkeypress(up, up_arrow)
turtle.onkeypress(down, down_arrow)
turtle.onkeypress(left, left_arrow)
turtle.onkeypress(right, right_arrow)
turtle.listen()
