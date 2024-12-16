import turtle
import random


class LightLine:
    """Class for light lines to create a space-like effect."""

    def __init__(self, x, y, length, vy, color):
        self.x = x
        self.y = y
        self.length = length
        self.vy = vy
        self.color = color

    def move(self, delta_time):
        """Move the light line vertically."""
        self.y += self.vy * delta_time

    def draw(self):
        """Draw the light line."""
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.pensize(1)
        turtle.pencolor(self.color)
        turtle.goto(self.x, self.y - self.length)
        turtle.penup()