from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, positions):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(positions)
        self.segments.append(new_segment)

    def reset_(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        current_heading = self.head.heading()
        # if current_heading != 270:
        #     self.segments[0].setheading(90)
        if current_heading == DOWN:
            return
        self.segments[0].setheading(UP)

    def down(self):
        current_heading = self.head.heading()
        if current_heading == UP:
            return
        self.segments[0].setheading(DOWN)

    def left(self):
        current_heading = self.head.heading()
        if current_heading == RIGHT:
            return
        self.segments[0].setheading(LEFT)

    def right(self):
        current_heading = self.head.heading()
        if current_heading == LEFT:
            return
        self.segments[0].setheading(RIGHT)
