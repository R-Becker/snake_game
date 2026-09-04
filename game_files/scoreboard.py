from turtle import Turtle
import time

# Location of the score display near the top of the window.
SCOREBOARD_X = 0
SCOREBOARD_Y = 270

# Load the saved high score when the program starts.
with open("highscore.txt", mode="r") as file:
    init_high_score = file.read()
    init_high_score = int(init_high_score)


class Scoreboard(Turtle):
    """Displays the current score, high score, and game status messages."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = init_high_score

        # Configure this Turtle to display text only.
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(SCOREBOARD_X, SCOREBOARD_Y)
        self.reset_scoreboard()

    def reset(self):
        """Save a new high score if needed, then reset the current score."""
        if self.score > self.high_score:
            self.high_score = self.score

            # Persist the high score so it is kept after the program closes.
            with open("highscore.txt", mode="w") as score:
                score.write(str(self.high_score))

        self.score = 0
        self.reset_scoreboard()

    def game_start_message(self):
        """Tell the player how to start the next game."""
        self.goto(0, 100)
        self.write(
            arg="Press SPACE to play",
            align="center",
            font=("Arial", 25, "normal")
        )

    def game_over_message(self):
        """Display a temporary game-over message."""
        self.goto(0, 100)
        self.pencolor("red")
        self.write(
            arg="GAME OVER",
            align="center",
            font=("Arial", 45, "normal")
        )

        # Force the message onto the screen before pausing.
        self.pencolor("white")
        self.getscreen().update()
        time.sleep(2.5)
        self.clear()

    def clear_game_over(self):
        """Clear status text and restore the normal score display."""
        self.clear()
        self.goto(SCOREBOARD_X, SCOREBOARD_Y)
        self.reset_scoreboard()

    def reset_scoreboard(self):
        """Redraw the current score and high score."""
        self.clear()
        self.goto(SCOREBOARD_X, SCOREBOARD_Y)
        self.write(
            arg=f"Score: {self.score} High Score: {self.high_score}",
            align="center",
            font=("Arial", 15, "normal")
        )

    def update_scoreboard(self):
        """Increase the score after food is collected and redraw it."""
        self.score += 1
        self.reset_scoreboard()