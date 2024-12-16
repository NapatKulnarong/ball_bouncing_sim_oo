MIDNIGHT SPACE
_______________________________________________________________________________________________
Description

Midnight Space is an arcade-style game that immerses players in the role of a spaceship pilot. 
The objective is to navigate through an infinite cosmic adventure by avoiding obstacles, 
collecting coins, and engaging in combat with UFOs. The game’s captivating visuals, immersive 
sound effects, and dynamic scoreboard provide an engaging and challenging experience that will 
test players’ reflexes and concentration.
_______________________________________________________________________________________________
Features
• Precise Navigation: Utilize the keyboard for seamless control of the spaceship.
• Evolving Challenges:
   - Dodge UFOs and suns
   - Collect coins
   - Fight UFOs with lasers to earn bonus coins.
• Comprehensive Scoreboard System: Monitors your highest scores and how they compare to others.
• Comprehensive Game Manual: Instructions are readily accessible upon the welcome screen.
• Captivating Visuals:
   - Stars descend like snowflakes, immersing you in a cosmic atmosphere.
   - Subtle light lines enhance the visual appeal of the background.
• Immersive Soundscape: An immersive soundtrack, featuring background music and sound effects.
_______________________________________________________________________________________________
Gameplay Overview

Controls
- Left Arrow: Move the spaceship to the left.
- Right Arrow: Move the spaceship to the right.
- Up Arrow: Fire lasers to destroy UFOs.

Objective
- Collect Coins: Each coin increases your balance.
- Destroy UFOs: Eliminate UFOs to earn bonus coins.
- Avoid Obstacles: Colliding with suns, or UFOs terminates the game.
- Travel Farther: Distance traveled is recorded and compared on the Scoreboard.

Game Over
Upon termination, your performance statistics will be displayed, including:
- Total Coins Collected and current Balance
- Distance Traveled
- Longest Distance Recorded
- Ranking compared to the top players.
_______________________________________________________________________________________________
Getting Started

1. Install Python : Ensure Python 3.12+ is installed on your system. 
   To check your version, type “python —version” in the terminal.

2. Install Pygame : Type “pip install pygame” in the terminal.

3. Add all the Python and CSV files : Locate them in the top folder.
    • run_ball.py, 
    • ball.py 
    • spaceship.py
    • sun.py     
    • ufo.py     
    • light_line.py     
    • border.py     
    • welcome.py     
    • user_manager.py
    • user_data.csv

4. Add all the game assets : Make sure that all the following sound files are placed 
   in the Sounds/ folder, located inside the top folder.
    • welcome.mp3 (welcome page background music)
    • mastermind.mp3 (in game background music)
    • coin.mp3 (coin collecting sound effect)
    • comet.mp3 (bouncing sound effect)
    • explode.mp3 (game over sound effect)
    • laser.mp3 (laser shooting sound effect)
    • hit.mp3 (comet collision sound)

5. Execute the main file : Type  “python run_ball.py”  in the terminal.
_______________________________________________________________________________________________
Usage

Demonstrate Video Link : https://youtu.be/bqQy8csVgvw
_______________________________________________________________________________________________
[Note : UML Class Diagram is provided in the GitHub repository]

Purpose of Each Class

1. LightLine : Represents the visual “lines of light” effect in the game background, 
   making the game feel more space-like.

   Attributes
   • x, y: Position
   • length: Length of the line.
   • vy: Vertical speed of the light line.
   • color: Color of the light line.

   Funtionality
   • Moves the light line vertically.
   • Renders the light line on the screen.
...............................................................................................
2. UFO : Represents an enemy UFO object in the game.

   Attributes
   • x, y: Position.
   • size: Size of the UFO.
   • vy: Vertical speed.

   Functionality
   • Moves the UFO downward.
   • Renders the UFO on the screen.
...............................................................................................
3. Spaceship : Represents the player’s spaceship.

   Attributes
   • width, height: Dimensions of the spaceship.
   • location: Current position of the spaceship.

   Functionality
   • Moves the spaceship horizontally.
   • Fires lasers.
   • Checks for collisions with objects.
...............................................................................................
4. Ball : Represents game objects like comets and coins.

   Attributes
   • x, y: Position.
   • vx, vy: Speed in the x and y directions.
   • type: Type of ball (e.g., comet or coin).
   • size: Size of the ball.

   Functionality
   • Moves the ball.
   • Renders the ball on the screen.
...............................................................................................
5. Sun : Represents a sun in the game that players must avoid.

   Attributes
   • x, y: Position.
   • size: Size of the sun.
   • vy: Vertical speed.

   Functionality
   • Moves the sun downward.
   • Renders the sun on the screen.
...............................................................................................
6. Border : Represents the space frame of the game.

   Functionality
   • Renders the game space frame (boundary).
...............................................................................................
7. UserManager : Manages user data (usernames, balances, high scores)

   Attributes
   • file_name: Path to the CSV file storing user data.

   Functionality
   • Get user data.
   • Updates user balance and longest distance.
   • Get top players based on distance.
...............................................................................................
8. WelcomePage : Displays the welcome screen.

   Attributes
   • file_path: Path to the user data file.
   • music_file: Path to the background music file.
   • stars: List of star objects for the falling star effect.
   • num_stars: Number of stars displayed on the welcome screen.

   Functionality
   • Plays background music.
   • Displays the welcome screen.
   • Animates falling stars.
   • Displays a game manual.
   • Handles user login and registration.
...............................................................................................
9. MidnightSpaceGame : The main game class that manages gameplay.

   Attributes
   • ball_list: List of Ball objects (comets, coins).
   • sun_list: List of Sun objects (hazards).
   • light_lines: List of LightLine objects (background effect).
   • ufo_list: List of UFO objects (enemies).
   • laser_list: List of lasers fired by the player.
   • spaceship: The player’s spaceship object.
   • coins_collected: Number of coins collected.
   • distance_traveled: Distance traveled in the game.
   • start_time: Start time of the game.
   • game_running: Flag indicating if the game is running.

   Functionality
   • Spawns game objects at intervals.
   • Updates positions of all objects.
   • Handles collisions between objects.
   • Displays the game over screen and leaderboard.
...............................................................................................
Interactions Between Each Object

• WelcomePage: Displays login screen and interacts with UserManager to validate or create user accounts.

• UserManager: Reads and writes user data to a CSV file and shares user information with MidnightSpaceGame.

• MidnightSpaceGame: Manages various objects, including Spaceships, Balls, Suns, UFOs, and LightLines. 
                     It updates their positions and checks for collisions during gameplay.
                     
• Spaceships: These objects fire lasers that interact with UFO objects. They also detect collisions 
              with the Sun, Ball, or UFO objects.
              
• Suns: These objects are hazards that end the game when collided with by Spaceships.
_______________________________________________________________________________________________
Extension and Modification of the Baseline Code

• The Comets and Coins in the game are modified from the ball.py file.
• The spaceship.py file is modified from the paddle.py file.
• The main file, which contains all the game logic and runs the program, is modified from run_ball.py.
• Added new object types (UFO, Sun, LightLine).
• Enhanced interactivity by allowing the player to press the up arrow key to shoot lasers.
• Implemented a welcome screen (WelcomePage) that prompts users to log in and provides the game manual.
• Added User management system (UserManager) to store user statistics.
• Added more Collision logic between multiple object types.
• Integrated Pygame for background music and sound effects.
_______________________________________________________________________________________________
Testing 
• Tested all the individual classes to ensure correct behavior.
• Tested all different collision logics between each object.
• Ensured that the welcome and game over screen displays correctly.

Known Bugs
• The game crashes if the specified music file is not found.
• Objects like Ball and UFO may occasionally overlap slightly without causing a collision.
• On some devices, the animation may lag if too many objects appear simultaneously on the screen.
_______________________________________________________________________________________________
Project Sophistication Level : 90
_______________________________________________________________________________________________
Future Enhancements
  • More game items and features such as diamonds, asteroids, black holes, double lasers.
  • Spaceship customization (skins, laser types).
  • More game maps
  • Multiplayer support
_______________________________________________________________________________________________
Credits
Developer : Napat Kulnarong   
Libraries Used in the project : Python Turtle, Pygame
Sounds
https://youtu.be/f7MiaSr-0ug?si=xHgu-ZrbbZIGaGTT
https://youtu.be/Tmz1lz0zcLQ?si=Y2MjSnYF53chzWV
https://youtu.be/RfkcI8dhfsQ?si=0G6VDNJXnx02JK6H
https://youtu.be/qZIZ9ZqqgjY?si=NAQqpAhDwL4Mg2yU
https://youtu.be/FuvmTL1nPDs?si=mAZnGewI1MixtfHs
https://youtu.be/JcG_ugrzfHE?si=kC_gqL91EzdYhPYk
_______________________________________________________________________________________________