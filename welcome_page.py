import turtle
import csv
import os
import random
import time
import pygame  # Import Pygame for background music


class Star:
    """Class for stars on the welcome page"""
    def __init__(self, x, y, size, vy):
        self.size = size
        self.x = x
        self.y = y
        self.vy = vy

    def move(self, delta_time):
        self.y += self.vy * delta_time  # Move downward

    def draw(self):
        """Draw the star."""
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.dot(self.size, "white")  # Small white dots for stars


class WelcomePage:
    def __init__(self, file_path, music_file):
        self.file_path = file_path
        self.music_file = music_file
        self.username = None
        self.data = self.load_user_data()
        self.stars = []
        self.num_stars = 130

    def load_user_data(self):
        """Load user data from the CSV file."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                file.write("username,balance\n")
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            return {row['username']: float(row['balance']) for row in reader}

    def save_new_user(self, username):
        """Save new username"""
        with open(self.file_path, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([username, 0])
        self.data[username] = 0

    def setup_screen(self):
        """Set up the welcome page."""
        screen = turtle.Screen()
        screen.title("MIDNIGHT SPACE")
        screen.setup(width=1200, height=800)
        screen.bgcolor("black")
        screen.tracer(0)  # Turn off automatic updates
        return screen

    def create_stars(self):
        """Generate stars randomly positioned"""
        for _ in range(self.num_stars):
            x = random.randint(-600, 600)
            y = random.randint(-400, 400)
            size = random.randint(2, 5)
            vy = random.uniform(-30, -10)  # Move speed downward
            self.stars.append(Star(x, y, size, vy))

    def update_stars(self, delta_time):
        """Move and redraw the stars."""
        for star in self.stars:
            star.move(delta_time)
            if star.y < -300:
                star.y = 300
                star.x = random.randint(-400, 400)
        self.draw_stars()

    def draw_stars(self):
        """Draw the stars."""
        for star in self.stars:
            star.draw()

    def play_music(self):
        """Play background music"""
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play(-1)  # Loop indefinitely

    def display_welcome_screen(self):
        """Display the welcome page"""
        self.play_music()

        screen = self.setup_screen()
        self.create_stars()

        # Game title display
        title_turtle = turtle.Turtle()
        title_turtle.hideturtle()
        title_turtle.penup()
        title_turtle.color("#FFFFFF")
        title_turtle.goto(0, 120)
        title_turtle.write("MIDNIGHT SPACE", align="center", font=("Courier", 72, "italic"))
        title_turtle.color("#1F8AFF")
        title_turtle.goto(-3, 117)
        title_turtle.write("MIDNIGHT SPACE", align="center", font=("Courier", 72, "italic"))

        # Game Manual display
        manual_turtle = turtle.Turtle()
        manual_turtle.hideturtle()
        manual_turtle.penup()
        manual_turtle.color("#6C707E")
        manual_turtle.goto(-270, -150)
        manual_text = [
            "1. Use LEFT and RIGHT arrow keys to move the spaceship.",
            "2. Press UP to shoot lasers at incoming UFOs.",
            "3. Collect coins to earn points.",
            "4. Avoid comets and suns. Colliding ends the game!",
            "5. Travel as far as possible to increase your distance.",
        ]

        for i, line in enumerate(manual_text):
            manual_turtle.goto(-270, -150 - (20 * i))
            manual_turtle.write(line, align="left", font=("Courier", 16, "normal"))

        # Main loop
        start_time = time.time()
        while True:
            delta_time = time.time() - start_time
            start_time = time.time()

            # Update and redraw the stars
            turtle.clear()  # Clear the screen before drawing new frame
            self.update_stars(delta_time)

            # Redraw title and game manual
            title_turtle.goto(-3, 117)
            title_turtle.write("MIDNIGHT SPACE", align="center", font=("Courier", 72, "italic"))
            for i, line in enumerate(manual_text):
                manual_turtle.goto(-270, -150 - (20 * i))
                manual_turtle.write(line, align="left", font=("Courier", 16, "normal"))

            # Prompt for username
            username = screen.textinput("Login", "Enter your username:")
            if username:
                username = username.strip()
                if username in self.data:
                    print(f"Welcome back, {username}! Your current balance is {self.data[username]} coins.")
                    self.username = username
                    break
                else:
                    confirm = screen.textinput("New User",
                                               f"Username '{username}' not found. Create new user? (yes/no)")
                    if confirm and confirm.lower() == "yes":
                        self.save_new_user(username)
                        print(f"New user '{username}' created with 0 coins.")
                        self.username = username
                        break

            if username is None:
                print("User canceled input. Exiting...")
                try:
                    screen.bye()
                except turtle.Terminator:
                    pass
                exit()

        # Stop music
        pygame.mixer.music.stop()
        screen.clear()
        return self.username, self.data.get(self.username, 0)


if __name__ == "__main__":
    music_file = "Sounds/welcome.mp3"
    welcome_page = WelcomePage("user_data.csv", music_file)
    username, balance = welcome_page.display_welcome_screen()
    print(f"Logged in as: {username} with balance: {balance}")

