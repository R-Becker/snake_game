# Snake Game

A recreation of the classic **Snake game built with Python and the Turtle graphics library**. The project uses object-oriented programming to separate the snake, food, scoreboard, and main game logic into individual components.

The player controls the snake using the arrow keys, collects food to increase their score and grow the snake, and tries to avoid colliding with the walls or the snake's own body. The program tracks the score for each game played and saves a high score. 

## Features

- Classic Snake gameplay
- Arrow-key movement controls
- Snake growth after collecting food
- Random food spawning
- Wall collision detection
- Self-collision detection
- Score tracking
- Persistent high-score system
- Game-over and restart functionality
- Object-oriented program structure

## Technologies Used

- **Python**
- **Turtle Graphics**
- Python file I/O

No external packages are required.

## Project Structure

```text
snake-game/
│
├── images/
│   ├── start_game.png
│   ├── game_playing.png
│   └── end_game.png
│
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
├── scores.txt
└── README.md
```

### `main.py`

Controls the overall game flow, including:

- Creating the game window
- Handling keyboard input
- Running the main game loop
- Detecting food, wall, and body collisions
- Starting and resetting games

### `snake.py`

Contains the `Snake` class and manages:

- Creating snake segments
- Moving the snake
- Changing direction
- Preventing direct reversal
- Growing the snake
- Resetting the snake after a game ends

### `food.py`

Contains the `Food` class, which creates the food object and moves it to a random location whenever the snake collects it.

### `scoreboard.py`

Contains the `Scoreboard` class and handles:

- Current score
- High score
- Game-start messages
- Game-over messages
- Saving the high score

### `scores.txt`

Stores the player's high score so that it remains available after the program is closed and restarted.

### `images/`

Contains screenshots demonstrating the different states of the game, including the start screen, active gameplay, and game-over screen.

## Controls

```text
| Key | Action |
| --- | --- |
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |
| Space | Start Game |
```

## What I Learned

This project helped me practice building a larger Python program using **object-oriented programming** rather than keeping all of the game logic in a single file.

Some of the concepts I worked with include:

- Designing classes with separate responsibilities
- Creating and managing objects
- Organizing a Python project across multiple files
- Handling keyboard events
- Implementing a continuous game loop
- Detecting collisions using object coordinates and distances
- Managing game state
- Reading from and writing to files
- Persisting data between program sessions

One challenge was managing the snake's movement and direction changes while preventing the player from immediately reversing into the snake's own body. The game tracks both the snake's current heading and its next requested heading so direction changes can be applied correctly during each frame.

## Possible Future Improvements

Some features that could be added in the future include:

- Difficulty levels
- Adjustable game speed
- Pause functionality
- Additional obstacles

## About This Project

I built this project as part of developing my Python programming skills, with an emphasis on **object-oriented design, program organization, and event-driven programming**. It provided experience turning individual Python concepts into a complete, and easy-to-play recreation of a game I've played growing up.
