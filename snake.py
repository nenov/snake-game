import turtle
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'lightblue']
DIAMOND = ((-10, 0), (0, 10), (10, 0), (0, -10))
turtle.register_shape('diamond', DIAMOND)


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape('diamond')
        self.last_input = self.head.heading()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color(COLORS[len(self.segments) - 1 % 8])
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.last_input = self.head.heading()

    def up(self):
        if self.last_input != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.last_input != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.last_input != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.last_input != LEFT:
            self.head.setheading(RIGHT)
