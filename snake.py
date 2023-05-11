from random import randrange
from turtle import *

from freegames import square, vector

import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
movefd = vector(0, -10)
n = random.randint(0, 9)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y
    "Cambia la direccion de la comida"
    movefd.x = (x)
    movefd.y = (y)

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def inside2(fd):
    """Return True if head inside boundaries."""
    return -200 < fd.x < 190 and -200 < fd.y < 190

def move():
    """Move snake forward one segment."""
    fdm = random.randint(0, 99)

    head = snake[-1].copy()
    head.move(aim)

    if(fdm == 1 or fdm == 59):
        food.x = randrange(-15, 15) * 10
        food.move(movefd)
        food.y = randrange(-15, 15) * 10
    

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.move
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        if(n == 0 or n == 5):
            square(body.x, body.y, 9, 'black')
            square(food.x, food.y, 9, 'green')
            update()
        elif(n == 1 or n == 6):
            square(body.x, body.y, 9, 'blue')
            square(food.x, food.y, 9, 'black')
            update()
        elif(n == 2 or n == 7):
            square(body.x, body.y, 9, 'pink')
            square(food.x, food.y, 9, 'cyan')
            update()
        elif(n == 3 or n == 8):
             square(body.x, body.y, 9, 'green')
             square(food.x, food.y, 9, 'blue')
             update()
        elif(n == 4 or n == 9):
             square(body.x, body.y, 9, 'cyan')
             square(food.x, food.y, 9, 'pink')
             update()

    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()