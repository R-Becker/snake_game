from turtle import Turtle
import time

# Starting coordinates for the three original snake segments.
STARTING_LOCATIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    """Controls the snake's segments, movement, direction, growth, and reset."""

    def __init__(self):
        self.segments = []
        self.create_segments()
        self.head = self.segments[0]

        # Track both the active direction and the next requested direction.
        # This prevents rapid key presses from making the snake reverse into itself.
        self.current_heading = 0
        self.next_heading = 0

    def create_segments(self):
        """Create the snake at its starting positions."""
        for location in STARTING_LOCATIONS:
            self.add_segment(location)

    def add_segment(self, location):
        """Create one body segment at the supplied location."""
        snake = Turtle(shape="square")
        snake.color("brown3")
        snake.penup()
        snake.goto(location)
        self.segments.append(snake)

    def extend(self):
        """Add a new segment to the end of the snake."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move each segment forward one position."""
        # Control the overall speed of the game.
        time.sleep(0.1)

        # Apply the newest valid direction once per frame.
        self.current_heading = self.next_heading
        self.head.setheading(self.current_heading)

        # Move each body segment into the previous segment's old position.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # Move the head forward after repositioning the body.
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Turn upward unless the snake is currently moving down."""
        if self.current_heading != 270:
            self.next_heading = 90

    def down(self):
        """Turn downward unless the snake is currently moving up."""
        if self.current_heading != 90:
            self.next_heading = 270

    def left(self):
        """Turn left unless the snake is currently moving right."""
        if self.current_heading != 0:
            self.next_heading = 180

    def right(self):
        """Turn right unless the snake is currently moving left."""
        if self.current_heading != 180:
            self.next_heading = 0

    def reset(self):
        """Remove the old snake and create a new snake at the starting position."""
        # Move old Turtle objects off-screen before removing their references.
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()
        self.create_segments()
        self.head = self.segments[0]

        # Every new game starts with the snake facing right.
        self.current_heading = 0
        self.next_heading = 0