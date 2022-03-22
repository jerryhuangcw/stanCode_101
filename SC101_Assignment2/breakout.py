"""
File: breakout.py
Name: Jerry Huang
stanCode Breakout Project adapted from Eric Roberts's Breakout
by Sonja Johnson-Yu, Kylie Jue, Nick Bowman,and Jerry Liao.

This program simulates the classic game Breakout Clone.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    bricks_left = graphics.bricks_count()  # number of bricks left

    # animation loop
    while True:
        pause(FRAME_RATE)
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())

        # lives count
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.reset_ball_position()
            lives -= 1
            if lives == 0:
                break

        # game progress
        if bricks_left == 0:
            break

        # window boarder bounce
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_opp_dx()
        if graphics.ball.y <= 0:
            graphics.set_opp_dy()

        # paddle bounce
        if graphics.ball.y >= graphics.window.height - graphics.get_paddle_offset() - 2*graphics.get_ball_radius():
            pad_1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + 2*graphics.get_ball_radius())
            pad_2 = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.get_ball_radius(),
                                                  graphics.ball.y + 2 * graphics.get_ball_radius())
            if graphics.paddle.x - graphics.get_ball_radius() < graphics.ball.x < \
                    graphics.paddle.x + graphics.paddle.width - graphics.get_ball_radius():  # right above board
                if pad_1 is not None or pad_2 is not None:
                    graphics.set_opp_dy()
                    if graphics.get_dy() > 0:
                        graphics.set_opp_dy()
            else:
                if pad_1 or pad_2 is not None:
                    graphics.set_opp_dx()

        # destroy bricks
        if graphics.ball.y < graphics.window.height - graphics.get_paddle_offset() - 2 * graphics.get_ball_radius():
            obj_1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + 2*graphics.get_ball_radius())
            obj_2 = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.get_ball_radius(),
                                                  graphics.ball.y + 2 * graphics.get_ball_radius())
            obj_3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            obj_4 = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.get_ball_radius(), graphics.ball.y + 2)
            if obj_1 is not None:
                graphics.window.remove(obj_1)
                bricks_left -= 1
                graphics.set_opp_dy()
            elif obj_2 is not None:
                graphics.window.remove(obj_2)
                bricks_left -= 1
                graphics.set_opp_dy()
            elif obj_3 is not None:
                graphics.window.remove(obj_3)
                bricks_left -= 1
                graphics.set_opp_dy()
            elif obj_4 is not None:
                graphics.window.remove(obj_4)
                bricks_left -= 1
                graphics.set_opp_dy()


if __name__ == '__main__':
    main()
