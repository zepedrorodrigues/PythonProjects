import turtle
from turtle import Turtle, Screen
import time
import random
import os


class Snake:
    def __init__(self):
        self.group = []
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        self.head = self.group[0]

    def create_snake(self):
        for position in self.starting_positions:
            self.add_block(position)

    def add_block(self, position):
        new_block = Turtle('square')
        new_block.width(4)
        new_block.color('white')
        new_block.penup()
        new_block.goto(position)
        new_block.setheading(0)
        self.group.append(new_block)

    def extend(self):
        self.add_block(self.group[-1].pos())

    def move(self):
        for x in range(len(self.group) - 1, 0, -1):
            self.group[x].goto(self.group[x - 1].pos())
        self.head.forward(20)
        time.sleep(0.1)

    def reset(self):
        for g in self.group:
            g.goto(500, 500)
        self.group.clear()
        self.create_snake()
        self.head = self.group[0]

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.width(4)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed('fastest')
        self.move()

    def move(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.color('white')
        self.hideturtle()
        self.highscore_file = os.path.join(os.path.dirname(__file__), "Highscore.txt")
        self.highscore = self.read_highscore()
        self.update_scoreboard()

    def collision_food(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} Highscore: {self.highscore}', align='center', font=('Arial', 15, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_highscore(self.highscore)
        self.score = 0
        self.update_scoreboard()

    def read_highscore(self):
        if os.path.exists(self.highscore_file):
            with open(self.highscore_file, 'r') as file:
                return int(file.read())
        return 0

    def write_highscore(self, highscore):
        with open(self.highscore_file, 'w') as file:
            file.write(str(highscore))


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake Game')
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.turn_up, 'Up')
    screen.onkey(snake.turn_right, 'Right')
    screen.onkey(snake.turn_left, 'Left')
    screen.onkey(snake.turn_down, 'Down')

    game_is_on = True
    while game_is_on:
        screen.update()
        snake.move()

        # Check for collision with food
        if snake.head.distance(food) < 15:
            food.move()
            snake.extend()
            scoreboard.collision_food()

        # Check for collision with wall
        if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or
                snake.head.ycor() > 290 or snake.head.ycor() < -290):
            scoreboard.reset()
            snake.reset()

        # Check for collision with self
        for block in snake.group[1:]:
            if snake.head.distance(block) < 10:
                scoreboard.reset()
                snake.reset()

    screen.mainloop()


if __name__ == "__main__":
    main()
