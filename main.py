import time
from turtle import Screen, Turtle

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

segment_1 = Turtle("square")
segment_1.color = "white"

segment_2 = Turtle("square")
segment_2.color = "white"

segment_3 = Turtle("square")
segment_3.color = "white"

segments = []

snake = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
score = 0
scoreboard.write_score()

while game_is_on:

    screen.update()
    snake.move()
    time.sleep(0.1)

    # food collision detection
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        scoreboard.write_score()
