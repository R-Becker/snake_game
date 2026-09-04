from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food


# Set up the main game window.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Turn off Turtle's automatic animation so the game can update one frame at a time.
screen.tracer(0)

# Create the main game objects.
scoreboard = Scoreboard()
snake = Snake()
food = Food()

# The game begins paused until the player presses SPACE.
game_running = False


def start_game():
    """Start or resume gameplay when SPACE is pressed."""
    global game_running

    if not game_running:
        game_running = True
        scoreboard.clear_game_over()


def end_game():
    """Stop the current game, reset its objects, and show the restart message."""
    global game_running

    game_running = False

    # Save/reset the score and rebuild the snake for the next game.
    scoreboard.reset()
    snake.reset()

    # Briefly show GAME OVER, then wait for the player to start again.
    scoreboard.game_over_message()
    scoreboard.game_start_message()


# Listen for keyboard input.
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="space", fun=start_game)

# Show instructions before the first game begins.
scoreboard.game_start_message()

game_is_on = True

# Main game loop.
while game_is_on:
    screen.update()

    # Only move the snake and check collisions while a game is active.
    if game_running:
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.update_scoreboard()

        # Detect collision with any edge of the 600x600 window.
        if (
            snake.head.xcor() > 299
            or snake.head.xcor() < -299
            or snake.head.ycor() > 299
            or snake.head.ycor() < -299
        ):
            end_game()

        # Detect collision between the snake's head and its body.
        for segment in snake.segments:
            # The head will always have distance 0 from itself, so skip it.
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                end_game()
                break

screen.exitonclick()