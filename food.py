from turtle import Turtle
import turtle
import random
image = "media/image.gif"
turtle.register_shape(image)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(image)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)