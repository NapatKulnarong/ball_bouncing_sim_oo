from spaceship import Spaceship
from ball import Ball
from sun import Sun
from border import Border
from light_line import LightLine
from ufo import UFO
from welcome_page import WelcomePage
from user_manager import UserManager
import turtle
import time
import random
import pygame


class MidnightSpaceGame:
    """Main class for the logic of the game"""
    def __init__(self, num_comets, num_coins, num_suns, username, user_manager):

        # Initialize background music and sound effects
        pygame.mixer.init()
        pygame.mixer.music.load("Sounds/mastermind.mp3")
        pygame.mixer.music.play(-1)
        self.coin_sound = pygame.mixer.Sound("Sounds/coin.mp3")
        self.explode_sound = pygame.mixer.Sound("Sounds/explode.mp3")
        self.laser_sound = pygame.mixer.Sound("Sounds/laser.mp3")
        self.comet_sound = pygame.mixer.Sound("Sounds/hit.mp3")
        self.comet_sound.set_volume(0.6)

        # Initialize required variables for game logic and items.
        self.num_comets = num_comets
        self.num_coins = num_coins
        self.num_suns = num_suns
        self.ball_list = []
        self.sun_list = []
        self.light_lines = []
        self.ufo_list = []
        self.laser_list = []
        self.coins_collected = 0
        self.distance_traveled = 0.0
        self.start_time = time.time()
        self.game_running = True
        self.username = username
        self.user_manager = user_manager

        # Timers
        self.spawn_timer = 0
        self.sun_timer = 0
        self.light_line_timer = 0

        # Set up screen
        turtle.setup(width=1200, height=800)
        turtle.bgcolor("black")
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)  # Set colormode to RGB
        self.canvas_width = 800
        self.canvas_height = 600

        # Initialize the space frame
        self.border = Border(self.canvas_width, self.canvas_height)
        self.border.draw()

        # Initialize objects
        for _ in range(self.num_comets):
            self.spawn_comet()
        for _ in range(self.num_coins):
            self.spawn_coin()
        for _ in range(self.num_suns):
            self.spawn_sun()

        # Initialize spaceship
        self.spaceship = Spaceship(50, 40)
        self.spaceship.set_location([0, -self.canvas_height // 2 + 100])

        self.screen = turtle.Screen()
        self.screen.title("Midnight Space Game")

    def move_left(self):
        """Move the spaceship left"""
        if self.spaceship.location[0] - self.spaceship.width // 2 > -self.canvas_width // 2:
            self.spaceship.set_location([self.spaceship.location[0] - 40, self.spaceship.location[1]])

    def move_right(self):
        """Move the spaceship right"""
        if self.spaceship.location[0] + self.spaceship.width // 2 < self.canvas_width // 2:
            self.spaceship.set_location([self.spaceship.location[0] + 40, self.spaceship.location[1]])

    def spawn_comet(self):
        """Spawn pastel colored comets randomly"""
        size = random.randint(10, 20)
        x = random.randint(-self.canvas_width // 2 + size, self.canvas_width // 2 - size)
        y = self.canvas_height // 2 - size
        vx = random.uniform(-3, 3)
        vy = random.uniform(-3, -1)
        color = (
            random.randint(150, 240),
            random.randint(150, 240),
            random.randint(150, 240),
        )
        self.ball_list.append(Ball(size, x, y, vx, vy, color, "comet"))

    def spawn_coin(self):
        """Spawn coins randomly"""
        size = 10
        x = random.randint(-self.canvas_width // 2 + size, self.canvas_width // 2 - size)
        y = self.canvas_height // 2 - size
        vy = random.uniform(-6, -4)
        self.ball_list.append(Ball(size, x, y, 0, vy, "#D4AF37", "coin"))

    def spawn_sun(self):
        """Spawn suns randomly"""
        max_suns = 5
        if len(self.sun_list) < max_suns:
            size = 15
            x = random.randint(-self.canvas_width // 2 + size, self.canvas_width // 2 - size)
            y = self.canvas_height // 2 - size
            vy = random.uniform(-2, 0)
            self.sun_list.append(Sun(x, y, size, vy))

    def spawn_light_line(self):
        """Spawn light lines randomly"""
        x = random.randint(-self.canvas_width // 2, self.canvas_width // 2)  # Random x position
        y = self.canvas_height // 2.8  # Start from the top
        length = random.randint(30, 80)  # Random length of the line
        vy = random.uniform(-7, -5)  # Speed of the line moving down

        # Provide colors for the light lines
        light_line_colors = [
            (33, 81, 133),
            (17, 49, 86),
            (11, 36, 74),
            (26, 67, 117),
        ]

        color = random.choice(light_line_colors)
        self.light_lines.append(LightLine(x, y, length, vy, color))

    def spawn_ufo(self):
        """Spawn UFOs randomly"""
        size = 20
        x = random.randint(-self.canvas_width // 2 + size, self.canvas_width // 2 - size)
        y = self.canvas_height // 2 - size
        vy = random.uniform(-9, -7)
        self.ufo_list.append(UFO(x, y, size, vy))

    def fire_laser(self):
        """Shoot laser and play sound effect"""
        laser = self.spaceship.shoot()
        self.laser_list.append(laser)
        self.laser_sound.play()

    def check_collisions(self):
        """Check collisions between objects and the spaceship."""
        for ball in self.ball_list[:]:
            if ball.type == "comet":
                if self.spaceship.collides_with(ball):
                    self.comet_sound.play()
                    speed_boost = 1.2
                    if abs(self.spaceship.location[0] - ball.x) < self.spaceship.width / 2:
                        ball.vy = abs(ball.vy) * speed_boost
                    if abs(self.spaceship.location[1] - ball.y) < self.spaceship.height / 2:
                        ball.vx = -ball.vx * speed_boost

                # Remove the comet if it moves out of the space frame
                if (ball.x - ball.size <= -self.canvas_width // 2 or
                        ball.x + ball.size >= self.canvas_width // 2 or
                        ball.y + ball.size >= self.canvas_height // 2 or
                        ball.y - ball.size <= -self.canvas_height // 2):
                    self.ball_list.remove(ball)

            elif ball.type == "coin":
                # Check if the coin collides with the spaceship
                if self.spaceship.collides_with(ball):
                    self.coins_collected += 1
                    self.coin_sound.play()
                    self.ball_list.remove(ball)

                # Remove the coin if it moves out of the space frame
                if (ball.x - ball.size <= -self.canvas_width // 2 or
                        ball.x + ball.size >= self.canvas_width // 2 or
                        ball.y + ball.size >= self.canvas_height // 2 or
                        ball.y - ball.size <= -self.canvas_height // 2):
                    self.ball_list.remove(ball)

                # Prevent the coin from moving out of the left/right frames
                elif ball.x - ball.size <= -self.canvas_width // 2 or ball.x + ball.size >= self.canvas_width // 2:
                    ball.vx = -ball.vx  # Reverse horizontal direction to stay within bounds

        # Check comet-to-comet collisions
        for i in range(len(self.ball_list)):
            for j in range(i + 1, len(self.ball_list)):
                ball1 = self.ball_list[i]
                ball2 = self.ball_list[j]

                dx = ball1.x - ball2.x
                dy = ball1.y - ball2.y
                distance = (dx ** 2 + dy ** 2) ** 0.5

                # If the comets are overlapping, handle the collision
                if distance <= ball1.size + ball2.size:
                    ball1.vx, ball2.vx = ball2.vx, ball1.vx
                    ball1.vy, ball2.vy = ball2.vy, ball1.vy

                    if distance > 0:
                        overlap = (ball1.size + ball2.size) - distance
                        ball1.x += (dx / distance) * (overlap / 2)
                        ball1.y += (dy / distance) * (overlap / 2)
                        ball2.x -= (dx / distance) * (overlap / 2)
                        ball2.y -= (dy / distance) * (overlap / 2)

                    # Ensure the comets remain within the screen bounds
                    ball1.x = max(min(ball1.x, 400 - ball1.size), -400 + ball1.size)
                    ball1.y = max(min(ball1.y, 300 - ball1.size), -300 + ball1.size)
                    ball2.x = max(min(ball2.x, 400 - ball2.size), -400 + ball2.size)
                    ball2.y = max(min(ball2.y, 300 - ball2.size), -300 + ball2.size)

        for sun in self.sun_list[:]:
            if self.spaceship.collides_with(sun):
                self.explode_sound.play()
                self.display_game_over_screen()
                self.game_running = False
                try:
                    self.screen.bye()
                except Exception:
                    pass
            elif sun.y - sun.size <= -self.canvas_height // 2:
                self.sun_list.remove(sun)

        # Check laser collisions with UFOs
        for laser in self.laser_list[:]:
            for ufo in self.ufo_list[:]:
                if abs(laser.x - ufo.x) < ufo.size and abs(laser.y - ufo.y) < ufo.size:
                    # Remove the laser
                    self.laser_list.remove(laser)

                    # Turn the UFO red
                    ufo.color = "red"
                    ufo.draw()
                    turtle.update()
                    time.sleep(0.1)

                    # Remove the UFO after showing the red effect
                    self.ufo_list.remove(ufo)
                    self.coins_collected += 10

        # Check UFO collisions with spaceship
        for ufo in self.ufo_list[:]:
            if self.spaceship.collides_with(ufo):
                self.explode_sound.play()
                self.display_game_over_screen()
                self.game_running = False
                break

    def display_game_over_screen(self):
        """Display a game over screen with stats and stop music."""
        pygame.mixer.music.stop()
        self.game_running = False
        self.user_manager.update_user_balance(self.username, self.coins_collected)
        self.user_manager.update_longest_distance(self.username, self.distance_traveled)

        # Get user data
        user_data = self.user_manager.get_user_data(self.username)
        total_balance = int(user_data.get("balance", 0))
        longest_distance = float(user_data.get("longest_distance", 0.0))

        turtle.clearscreen()
        turtle.bgcolor("#030B18")

        text_turtle = turtle.Turtle()
        text_turtle.hideturtle()
        text_turtle.penup()
        text_turtle.color("white")

        text_turtle.goto(0, 160)
        text_turtle.write("GAME OVER", align="center", font=("Courier", 96, "normal"))

        self.display_scoreboard_table()

        stats_x = 130
        stats_y = 55
        line_spacing = 35

        font_size = 24
        text_turtle.goto(stats_x, stats_y)
        text_turtle.write(f"Player: {self.username}", align="left", font=("Courier", 28, "normal"))

        text_turtle.goto(stats_x, stats_y - line_spacing)
        text_turtle.write(f"------------------", align="left",
                          font=("Courier", font_size, "normal"))

        text_turtle.goto(stats_x, stats_y - line_spacing * 2)
        text_turtle.write(f"Distance: {self.distance_traveled:.2f} km", align="left",
                          font=("Courier", font_size, "normal"))

        text_turtle.goto(stats_x, stats_y - line_spacing * 3)
        text_turtle.write(f"Longest: {longest_distance:.2f} km", align="left",
                          font=("Courier", font_size, "normal"))

        text_turtle.goto(stats_x, stats_y - line_spacing * 4)
        text_turtle.write(f"------------------", align="left",
                          font=("Courier", font_size, "normal"))

        text_turtle.goto(stats_x, stats_y - line_spacing * 5)
        text_turtle.write(f"Coins: {self.coins_collected} coins", align="left", font=("Courier", font_size, "normal"))

        text_turtle.goto(stats_x, stats_y - line_spacing * 6)
        text_turtle.write(f"Balance: {total_balance} coins", align="left", font=("Courier", font_size, "normal"))

        turtle.update()
        time.sleep(3)
        self.screen.bye()

    def display_scoreboard_table(self):
        """Display the top 10 players"""
        table_turtle = turtle.Turtle()
        table_turtle.hideturtle()
        table_turtle.penup()
        table_turtle.color("white")

        # Table Header
        table_x = -420
        table_y = 70
        table_turtle.goto(table_x, table_y)
        table_turtle.write("Rank    Username         Distance (km)", align="left", font=("Courier", 18, "bold"))
        table_turtle.goto(table_x-5, table_y - 10)
        table_turtle.pendown()
        table_turtle.forward(420)  # Draw a line
        table_turtle.penup()

        # Table Content
        top_players = self.user_manager.get_top_players()
        y_offset = table_y - 50
        for idx, player in enumerate(top_players):
            table_turtle.goto(table_x, y_offset)
            try:
                longest_distance = float(player['longest_distance'])
                table_row = f" {idx + 1:<7} {player['username']:<18} {longest_distance:>10.2f}"
            except ValueError:
                table_row = f" {idx + 1:<7} {player['username']:<18} Invalid"
            table_turtle.write(table_row, align="left", font=("Courier", 18, "normal"))
            y_offset -= 30

    def redraw(self):
        turtle.clear()

        # Draw light lines (background)
        for line in self.light_lines:
            line.draw()

        # Draw spaceship, balls, suns, UFOs, and lasers
        self.spaceship.draw()

        for ball in self.ball_list:
            ball.draw()

        for sun in self.sun_list:
            sun.draw()

        for ufo in self.ufo_list:
            ufo.draw()

        for laser in self.laser_list:
            laser.draw()

        # Display distance and coins
        elapsed_time = time.time() - self.start_time
        self.distance_traveled = round(elapsed_time * 7.8, 1)
        turtle.penup()
        turtle.color("white")
        turtle.goto(-self.canvas_width // 2, self.canvas_height // 2 + 20)  # Adjusted top-left position
        turtle.write(f"COINS: {self.coins_collected} $", align="left", font=("Courier", 17, "bold"))

        turtle.goto(-self.canvas_width // 2 + 140, self.canvas_height // 2 + 20)  # Positioned closer
        turtle.write(f"DISTANCE: {self.distance_traveled:.2f} km", align="left", font=("Courier", 17, "bold"))

        turtle.hideturtle()
        turtle.update()

    def run(self):
        self.screen.listen()
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")
        self.screen.onkey(self.fire_laser, "Up")

        light_line_timer = 0

        while self.game_running:
            self.spawn_timer += 1
            light_line_timer += 1

            if light_line_timer % 20 == 0:
                self.spawn_light_line()

            if self.spawn_timer % 175 == 0:
                self.spawn_comet()
                self.spawn_coin()

            if self.sun_timer % 670 == 0:
                self.spawn_sun()

            for ball in self.ball_list:
                ball.move(0.1)

            for sun in self.sun_list:
                sun.move()

            for line in self.light_lines[:]:
                line.move(0.1)
                if line.y - line.length <= -self.canvas_height // 2:
                    self.light_lines.remove(line)

            if random.randint(1, 350) == 1:
                self.spawn_ufo()

            # Move UFOs
            for ufo in self.ufo_list[:]:
                ufo.move(0.1)

                # Remove UFO if it moves out of the bottom space frame
                if ufo.y - ufo.size <= -self.canvas_height // 2:  # Bottom boundary
                    self.ufo_list.remove(ufo)  # Remove UFO from the list

            # Move lasers
            for laser in self.laser_list[:]:
                laser.move()
                if laser.y > self.canvas_height // 2:  # Remove laser if it moves out of the space frame
                    self.laser_list.remove(laser)

            self.check_collisions()
            self.redraw()


# Main execution
if __name__ == "__main__":
    # Step 1: Display the welcome page
    welcome_page = WelcomePage("user_data.csv", music_file="Sounds/welcome.mp3")
    username, balance = welcome_page.display_welcome_screen()

    # Step 2: Initialize UserManager and load user information
    user_manager = UserManager("user_data.csv")
    print(f"Welcome {username}! Your current balance is {balance} coins.")

    # Step 3: Start game
    game = MidnightSpaceGame(
        num_comets=5,
        num_coins=3,
        num_suns=1,
        username=username,
        user_manager=user_manager
    )
    game.run()
