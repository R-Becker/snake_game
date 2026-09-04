from turtle import Turtle
import random

class Food(Turtle):
    """Represents the food object that the snake collects."""

    def __init__(self):
        super().__init__()

        # Configure the appearance of the food.
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")

        # Place the first food item at a random location.
        self.refresh()

    def refresh(self):
        """Move the food to a random position inside the game window."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
