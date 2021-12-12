from turtle import Screen
from score4snake import Scoreboard
from snake import Snake
from food4snake import Food
import time


# setting up window
window = Screen()
window.setup(width=600, height=600)
window.bgcolor("gray")
window.title("Classic Snake")
window.tracer(0)


# characters
snake = Snake()
food = Food()
score = Scoreboard()


# controlling snake
window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    window.update()
    time.sleep(0.1)


    snake.move()
    # detect collision with wall
    if snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # collision with tail
    # for seg in snake.segment:
    #     if seg == snake.head:
    #         continue
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            score.game_over()


window.exitonclick()
