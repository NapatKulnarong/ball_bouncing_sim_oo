import turtle
import math


class Sun:
    """Class for the sun"""

    def __init__(self, x, y, size, vy):
        self.x = x
        self.y = y
        self.size = size
        self.vy = vy

    def move(self):
        """Move the Sun downward."""
        self.y += self.vy

    def draw(self):
        # Draw a circle (center)
        turtle.penup()
        turtle.goto(self.x, self.y - self.size)
        turtle.fillcolor("#FFD700")
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

        # Draw rays
        turtle.color("#FFA500")
        for angle in range(0, 360, 30):
            ray_start_x = self.x + (self.size + 3) * math.cos(math.radians(angle))
            ray_start_y = self.y + (self.size + 3) * math.sin(math.radians(angle))
            ray_end_x = self.x + (self.size + 10) * math.cos(math.radians(angle))
            ray_end_y = self.y + (self.size + 10) * math.sin(math.radians(angle))

            turtle.penup()
            turtle.goto(ray_start_x, ray_start_y)
            turtle.pendown()
            turtle.goto(ray_end_x, ray_end_y)
            turtle.penup()
