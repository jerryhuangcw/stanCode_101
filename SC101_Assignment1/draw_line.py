"""
File: draw_line.py
Name: Jerry Huang
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


# global variables
window = GWindow()
count = 0  # mouse click counts
dot_x = 0
dot_y = 0


SIZE = 16  # This constant controls the diameter of the dot


def main():
    """
    This program allows user to draw lines on the window.
    The first click will show a dot on the canvas indicating the starting point of the line.
    The second click will be the end point of the line and will also remove the previous starting dot.
    Line drawing process is repeatable.
    """
    onmouseclicked(draw)


def draw(m):
    global dot_x, dot_y, count
    dot = GOval(SIZE, SIZE, x=m.x - SIZE / 2, y=m.y - SIZE / 2)
    window.add(dot)
    count += 1
    if count % 2 == 1 and count >= 0:  # first click condition
        dot_x = dot.x
        dot_y = dot.y
    elif count % 2 == 0 and count >= 0:  # second click condition
        d_dot = window.get_object_at(dot_x + SIZE / 2, dot_y + SIZE / 2)  # locate the starting dot
        window.remove(d_dot)
        line = GLine(dot_x + SIZE / 2, dot_y + SIZE / 2, m.x, m.y)
        window.add(line)
        window.remove(dot)


if __name__ == "__main__":
    main()
