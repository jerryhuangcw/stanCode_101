"""
File: extension_breakout.py
Name: Jerry Huang
stanCode Breakout Project adapted from Eric Roberts's Breakout
by Sonja Johnson-Yu, Kylie Jue, Nick Bowman,and Jerry Liao.

This extension program simulates the classic game Breakout Clone.
"""

from campy.gui.events.timer import pause
from campy.graphics.gobjects import GLabel
from extension_breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    bricks_left = graphics.bricks_count()  # number of bricks left

    # count for score board label
    bricks_num = GLabel(bricks_left)
    bricks_num.font = "arial-12"
    graphics.window.add(bricks_num, 110, graphics.window.height - 10)

    # count for live board label
    live_num = GLabel(lives)
    live_num.font = "arial-12"
    graphics.window.add(live_num, graphics.window.width - 19, graphics.window.height - 10)

    # animation loop
    while True:
        pause(FRAME_RATE)
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())

        # lives count
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:

            lives -= 1
            graphics.window.remove(live_num)  # update lives count
            live_num = GLabel(lives)
            live_num.font = "arial-12"
            graphics.window.add(live_num, graphics.window.width - 19, graphics.window.height - 10)
            if lives == 0:
                game_over = GLabel("GAME OVER")
                game_over.font = "arial-30"
                game_over.color = 'firebrick'
                graphics.window.add(game_over, graphics.window.width / 2 - 130, graphics.window.height / 2)
                break
            graphics.reset_ball_position()
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
                graphics.window.remove(obj_1)  # update bricks count
                bricks_left -= 1
                graphics.window.remove(bricks_num)
                bricks_num = GLabel(bricks_left)
                bricks_num.font = "arial-12"
                graphics.window.add(bricks_num, 110, graphics.window.height - 10)
                graphics.set_opp_dy()
            elif obj_2 is not None:
                graphics.window.remove(obj_2)  # update bricks count
                bricks_left -= 1
                graphics.window.remove(bricks_num)
                bricks_num = GLabel(bricks_left)
                bricks_num.font = "arial-12"
                graphics.window.add(bricks_num, 110, graphics.window.height - 10)
                graphics.set_opp_dy()
            elif obj_3 is not None:
                graphics.window.remove(obj_3)  # update bricks count
                bricks_left -= 1
                graphics.window.remove(bricks_num)
                bricks_num = GLabel(bricks_left)
                bricks_num.font = "arial-12"
                graphics.window.add(bricks_num, 110, graphics.window.height - 10)
                graphics.set_opp_dy()
            elif obj_4 is not None:
                graphics.window.remove(obj_4)  # update bricks count
                bricks_left -= 1
                graphics.window.remove(bricks_num)
                bricks_num = GLabel(bricks_left)
                bricks_num.font = "arial-12"
                graphics.window.add(bricks_num, 110, graphics.window.height - 10)
                graphics.set_opp_dy()


if __name__ == '__main__':
    main()
