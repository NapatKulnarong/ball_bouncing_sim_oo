import turtle


class LaserRay:
    """Class to represent a laser"""
    def __init__(self, x, y, vy=15):
        self.x = x
        self.y = y
        self.vy = vy

    def move(self):
        """Move the laser upward."""
        self.y += self.vy

    def draw(self):
        """Draw the laser."""
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color("red")
        turtle.pensize(2)
        turtle.goto(self.x, self.y + 10)
        turtle.penup()


class Spaceship:
    """Spaceship class."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.location = [0, 0]

    def set_location(self, location):
        """Set the spaceship's location."""
        self.location = location

    def move_left(self):
        """Move spaceship left."""
        self.location[0] -= 20

    def move_right(self):
        """Move spaceship right."""
        self.location[0] += 20

    def collides_with(self, obj):
        """Check for collision with another object."""
        return abs(self.location[0] - obj.x) < self.width and abs(self.location[1] - obj.y) < self.height

    def shoot(self):
        """Release a laser ray."""
        laser = LaserRay(self.location[0], self.location[1] + self.height // 2)
        return laser

    def draw(self):
        """Draw the spaceship."""
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.pendown()
        turtle.color("gray")
        turtle.fillcolor("gray")
        turtle.begin_fill()
        turtle.goto(self.location[0] - self.width // 2, self.location[1] - self.height // 2)
        turtle.goto(self.location[0], self.location[1] + self.height // 2)
        turtle.goto(self.location[0] + self.width // 2, self.location[1] - self.height // 2)
        turtle.goto(self.location[0], self.location[1])
        turtle.end_fill()
