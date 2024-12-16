import turtle


class Border:
    """Class to handle the static border of the game."""

    def __init__(self, canvas_width, canvas_height):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.border_turtle = turtle.Turtle()

    def draw(self):
        """Draw the space frame and fill in with a different color."""
        self.border_turtle.penup()
        self.border_turtle.hideturtle()

        self.border_turtle.color("#030B18")
        self.border_turtle.begin_fill()
        self.border_turtle.goto(-self.canvas_width // 2, -self.canvas_height // 2)
        self.border_turtle.pendown()

        for _ in range(2):
            self.border_turtle.forward(self.canvas_width)
            self.border_turtle.left(90)
            self.border_turtle.forward(self.canvas_height)
            self.border_turtle.left(90)
        self.border_turtle.end_fill()

        self.border_turtle.penup()
        self.border_turtle.goto(-self.canvas_width // 2, -self.canvas_height // 2)
        self.border_turtle.pendown()
        self.border_turtle.color("white")
        self.border_turtle.pensize(4)
        for _ in range(2):
            self.border_turtle.forward(self.canvas_width)
            self.border_turtle.left(90)
            self.border_turtle.forward(self.canvas_height)
            self.border_turtle.left(90)