from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.new_x =self.xcor()
        self.new_y=0

    def go_up(self):
        self.new_y = self.new_y + 20
        # new_y=new_y+20
        self.goto(x=self.xcor(), y=self.new_y)

    def go_down(self):
        self.new_y = self.new_y - 20
        # new_y = new_y - 20
        self.goto(x=self.xcor(), y=self.new_y)