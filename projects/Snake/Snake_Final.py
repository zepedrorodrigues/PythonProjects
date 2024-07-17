from turtle import *
from Snake_Modules import *
import time

screen = Screen()
screen.bgcolor('black'); screen.setup(width=600,height=600); screen.tracer(0)

snake = Snake(); food = Food(); score = Scoreboard(); 
border = Turtle(); border.color('white');border.penup();border.goto(290,290);border.hideturtle(); border.setheading(180); border.pendown()
for x in range(4):
    border.forward(580); border.left(90)

screen.listen(); screen.onkey(snake.turn_up,'Up');screen.onkey(snake.turn_down,'Down');screen.onkey(snake.turn_left,'Left');screen.onkey(snake.turn_right,'Right')
screen.listen(score.reset,'Enter');screen.listen(snake.reset,'Enter')
screen.tracer(0)

game_on = True

while game_on == True:
    snake.move()
    screen.update()
    if snake.head.distance(food)<15:
        snake.extend()
        food.move()
        score.collision_food()
    elif snake.head.xcor()>275 or snake.head.xcor()<-275 or snake.head.ycor()>275 or snake.head.ycor()<-275:
        snake.reset(); score.reset()
    else:
        for g in snake.group[1:len(snake.group)]:
            if snake.head.distance(g)<12:
                snake.reset(); score.reset()

screen.exitonclick()