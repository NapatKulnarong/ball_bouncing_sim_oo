import turtle
from ball import Ball


class UFO(Ball):
    """Class for the UFO"""

    def __init__(self, x, y, size, vy):
        super().__init__(size * 0.8, x, y, 0, vy, "lightgreen", "ufo")
        self.ring_length = size * 2.8
        self.ring_thickness = size * 0.15

    def draw(self):
        # Draw the circle
        turtle.penup()
        turtle.goto(self.x, self.y - self.size)
        turtle.pendown()
        turtle.color(self.color)
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

        # Draw the ring
        turtle.penup()
        turtle.goto(self.x - self.ring_length / 2, self.y - self.ring_thickness / 2)
        turtle.pendown()
        turtle.color("darkgreen")
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(self.ring_length)
            turtle.left(90)
            turtle.forward(self.ring_thickness)
            turtle.left(90)
        turtle.end_fill()
        