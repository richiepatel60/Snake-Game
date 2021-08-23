from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0

        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as new_data:
                new_data.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
