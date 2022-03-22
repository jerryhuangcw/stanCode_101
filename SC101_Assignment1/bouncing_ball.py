"""
File: bouncing_ball.py
Name: Jerry Huang
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# constant
VX = 3  # speed of x
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# global var
window = GWindow(700, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
ball.fill_color = "Black"
window.add(ball)
count = 0
click_switch = True


def main():
    """
    The ball will free fall from the initial position and bounce
    when it hit the floor after a mouse click. The mouse click won't affect the movement.
    The ball will return to the initial position after it is out of bound.
    The program will stop after the free fall process is processed 3 times.
    """
    onmouseclicked(bounce)


def bounce(m):  # To Sam: How can I solve this not-used parameter "m" issue?
    global count, click_switch
    if click_switch is True and count <= 2:
        vy = 0
        v_ground = 0  # terminal velocity when the ball hit the ground
        click_switch = False
        while True:
            vy += GRAVITY
            ball.move(VX, vy)
            if ball.y + SIZE <= window.height:
                v_ground = vy
            elif ball.y + SIZE >= window.height:
                vy = -v_ground * REDUCE
            pause(DELAY)
            if ball.x >= window.width:  # re-position
                ball.x = START_X
                ball.y = START_Y
                count += 1
                click_switch = True
                break


if __name__ == "__main__":
    main()
