from turtle import Turtle
import random
from ball import Ball

COLORS = ['light blue', 'royal blue',
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue',
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink',
              'medium sea green', 'khaki']

weights = [1, 2, 1, 1, 3, 2, 1, 4, 1, 3,
           1, 1, 1, 4, 1, 3, 2, 2, 1, 2,
           1, 2, 1, 2, 1]


class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.goto(x=x_cor, y=y_cor)

        self.quantity = random.choice(weights)

        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15


class Bricks:
    def __init__(self):
        self.y_start = 0
        self.y_end = 240
        self.bricks = []
        self.create_all_lanes()

    def create_lane(self, y_cor):
        for i in range(-570, 570, 63):
            brick = Brick(i, y_cor)
            self.bricks.append(brick)

    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 32):
            self.create_lane(i)
