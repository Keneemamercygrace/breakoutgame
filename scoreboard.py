from turtle import Turtle

FONT = ('arial', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self, lives):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.highScore = self.score
        self.goto(x=-580, y=260)
        self.lives = lives
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | Highest Score: {self.highScore} \
        | Lives: {self.lives}", align='left', font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.highScore:
            self.highScore += 1
        self.update_score()

    def decrease_lives(self):
        self.lives -= 1
        self.update_score()

    def reset(self):
        self.clear()
        self.score = 0
        self.update_score()
