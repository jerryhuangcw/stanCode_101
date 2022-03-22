"""
File: breakoutgraphics.py
Name: Jerry Huang
stanCode Breakout Project adapted from Eric Roberts's Breakout
by Sonja Johnson-Yu, Kylie Jue, Nick Bowman, and Jerry Liao.

This program simulates the classic game Breakout Clone.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# global var
game_switch = True

# control constants
BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 3  # Initial vertical speed for the ball.
MAX_X_SPEED = 3  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window.width - self.paddle.width) / 2,
                        self.window.height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2,
                        (self.window.height - self.ball.height) / 2)

        # Draw bricks
        self.brick_cols = BRICK_COLS
        self.brick_rows = BRICK_ROWS
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i == 0 or i == 1:
                    self.brick.color = 'red'
                    self.brick.fill_color = 'red'
                elif i == 2 or i == 3:
                    self.brick.color = 'orange'
                    self.brick.fill_color = 'orange'
                elif i == 4 or i == 5:
                    self.brick.color = 'yellow'
                    self.brick.fill_color = 'yellow'
                elif i == 6 or i == 7:
                    self.brick.color = 'green'
                    self.brick.fill_color = 'green'
                else:
                    self.brick.color = 'blue'
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, (0 + j * (brick_width + brick_spacing)),
                                brick_offset + i * (brick_height + brick_spacing))

        # Default initial velocity for the ball
        self._dx = 0
        self._dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.move_pad)
        onmouseclicked(self.game_play)

    def game_play(self, e):
        global game_switch
        if game_switch is True:
            self.set_ball_velocity(self)
            game_switch = False

    def reset_ball_position(self):
        global game_switch
        self._dx = 0
        self._dy = 0
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        game_switch = True

    def set_ball_velocity(self, e):
        self._dx = random.randint(1, MAX_X_SPEED)
        self._dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self._dx = -self._dx

    def move_pad(self, event):
        if self.paddle.width / 2 <= event.x <= self.window.width - self.paddle.width / 2:
            self.paddle.x = event.x - self.paddle.width / 2

    def get_dx(self):
        return self._dx

    def get_dy(self):
        return self._dy

    def set_opp_dx(self):
        self._dx *= -1

    def set_opp_dy(self):
        self._dy *= -1

    def bricks_count(self):
        b_count = self.brick_rows * self.brick_cols
        return b_count

    @staticmethod
    def get_paddle_offset():
        return PADDLE_OFFSET

    @staticmethod
    def get_ball_radius():
        return BALL_RADIUS
