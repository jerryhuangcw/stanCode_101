"""
File: my_drawing.py
Name: Jerry Huang
----------------------
This file uses campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GPolygon, GArc,  GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Crayon Shin Chan is one of my favorite cartoon charter.
    """
    window = GWindow(width=800, height=650, title="My face")
    label = GLabel("CRAYON SHIN CHAN", x=30, y=50)
    label.font = "arial-20"
    label.color = "RED"
    window.add(label)

    mouth = GOval(100, 70, x=180, y=470)
    mouth.filled = True
    mouth.fill_color = 'firebrick'
    window.add(mouth)

    jaw = GOval(240, 240, x=50, y=330)
    jaw.filled = True
    jaw.fill_color = 'lightsalmon'
    jaw.color = 'lightsalmon'
    window.add(jaw)

    head = GOval(500, 450, x=180, y=80)
    head.filled = True
    head.fill_color = 'lightsalmon'
    head.color = 'lightsalmon'
    window.add(head)

    cheek = GPolygon()
    cheek.add_vertex((170, 570))  # 1
    cheek.add_vertex((580, 520))  # 2
    cheek.add_vertex((575, 430))  # 3
    cheek.add_vertex((165, 480))  # 4
    cheek.filled = True
    cheek.fill_color = 'lightsalmon'
    cheek.color = 'lightsalmon'
    window.add(cheek)

    ear = GPolygon()
    ear.add_vertex((575, 520))  # 1
    ear.add_vertex((730, 530))  # 2
    ear.add_vertex((720, 350))  # 3
    ear.add_vertex((575, 420))  # 4
    ear.filled = True
    ear.fill_color = 'lightsalmon'
    ear.color = 'lightsalmon'
    window.add(ear)

    hair2 = GPolygon()
    hair2.add_vertex((590, 420))  # 1
    hair2.add_vertex((680, 370))  # 2
    hair2.add_vertex((677, 200))  # 3
    hair2.add_vertex((650, 150))  # 4
    hair2.add_vertex((550, 80))  # 5
    hair2.add_vertex((200, 80))  # 6
    hair2.add_vertex((200, 160))  # 7
    hair2.add_vertex((530, 160))  # 8
    hair2.add_vertex((570, 180))  # 9
    hair2.add_vertex((590, 210))  # 10
    hair2.filled = True
    hair2.fill_color = 'black'
    window.add(hair2)

    hair3 = GOval(40, 80, x=180, y=80)
    hair3.filled = True
    hair3.fill_color = 'black'
    window.add(hair3)

    mouth = GOval(100, 70, x=180, y=470)
    mouth.filled = True
    mouth.fill_color = 'firebrick'
    window.add(mouth)

    l_eyelash = GArc(125, 190, -10, 160, x=258, y=210)
    window.add(l_eyelash)

    r_eyelash = GArc(125, 190, 10, 170, x=418, y=230)
    window.add(r_eyelash)

    l_eye = GOval(120, 110, x=250, y=250)
    l_eye.filled = True
    l_eye.fill_color = "black"
    window.add(l_eye)

    r_eye = GOval(120, 110, x=410, y=265)
    r_eye.filled = True
    r_eye.fill_color = "black"
    window.add(r_eye)

    l_pupil = GOval(50, 48, x=285, y=280)
    l_pupil.filled = True
    l_pupil.fill_color = 'white'
    window.add(l_pupil)

    r_pupil = GOval(50, 48, x=445, y=295)
    r_pupil.filled = True
    r_pupil.fill_color = 'white'
    window.add(r_pupil)

    l_brow1 = GOval(25, 25, x=270, y=185)
    l_brow1.filled = True
    l_brow1.fill_color = "black"
    window.add(l_brow1)

    l_brow2 = GOval(25, 25, x=335, y=162)
    l_brow2.filled = True
    l_brow2.fill_color = "black"
    window.add(l_brow2)

    l_brow3 = GOval(25, 25, x=360, y=200)
    l_brow3.filled = True
    l_brow3.fill_color = "black"
    window.add(l_brow3)

    l_brow4 = GPolygon()
    l_brow4.add_vertex((271, 191))  # 1
    l_brow4.add_vertex((285, 208))  # 2
    l_brow4.add_vertex((350, 185))  # 3
    l_brow4.add_vertex((361, 212))  # 4
    l_brow4.add_vertex((378, 200))  # 5
    l_brow4.add_vertex((353, 163))  # 6
    l_brow4.filled = True
    l_brow4.fill_color = 'black'
    window.add(l_brow4)

    r_brow1 = GOval(25, 25, x=430, y=200)
    r_brow1.filled = True
    r_brow1.fill_color = "black"
    window.add(r_brow1)

    r_brow2 = GOval(25, 25, x=495, y=175)
    r_brow2.filled = True
    r_brow2.fill_color = "black"
    window.add(r_brow2)
    #
    r_brow3 = GOval(25, 25, x=520, y=215)
    r_brow3.filled = True
    r_brow3.fill_color = "black"
    window.add(r_brow3)
    #
    r_brow4 = GPolygon()
    r_brow4.add_vertex((431, 206))  # 1
    r_brow4.add_vertex((445, 223))  # 2
    r_brow4.add_vertex((510, 200))  # 3
    r_brow4.add_vertex((521, 227))  # 4
    r_brow4.add_vertex((538, 215))  # 5
    r_brow4.add_vertex((513, 175))  # 6
    r_brow4.filled = True
    r_brow4.fill_color = 'black'
    window.add(r_brow4)


if __name__ == '__main__':
    main()
