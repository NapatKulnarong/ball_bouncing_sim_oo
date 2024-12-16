import turtle


class Ball:
    """Class for comets and coins."""

    def __init__(self, size, x, y, vx, vy, color, ball_type):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.type = ball_type

    def move(self, delta_time):
        self.x += self.vx * delta_time
        self.y += self.vy * delta_time

    def draw(self):
        """Draw the ball."""
        turtle.penup()
        turtle.goto(self.x, self.y - self.size)
        turtle.color(self.color)
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()