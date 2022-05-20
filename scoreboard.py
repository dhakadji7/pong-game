from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self,position):
        super().__init__()
        self.score=0
        self.goto(position)
        self.color("white")
        self.write(f"Score:{self.score}",align="center",font=("Courier",18,"normal"))
        self.hideturtle()
        self.penup()


    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Courier", 18, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 18, "normal"))
