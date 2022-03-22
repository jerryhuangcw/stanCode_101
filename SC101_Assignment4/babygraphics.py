"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue', 'magenta']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * (width-2*GRAPH_MARGIN_SIZE) / len(YEARS)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # Top Boundary
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,)
    # Bottom Boundary
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    # Left Boundary
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    # Separation
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW, font='times')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    baby_d = name_data
    search_lst = lookup_names
    for i in range(len(search_lst)):
        for j in range(len(YEARS)-1):
            if str(YEARS[j]) in baby_d[search_lst[i]] and str(YEARS[j+1]) in baby_d[search_lst[i]]:
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j),
                                   GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)
                                   * int(baby_d[search_lst[i]][str(YEARS[j])]) / 1000,
                                   get_x_coordinate(CANVAS_WIDTH, j+1),
                                   GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)
                                   * int(baby_d[search_lst[i]][str(YEARS[j+1])]) / 1000, width=LINE_WIDTH,
                                   fill=str(COLORS[i % len(COLORS)]))
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX,
                                   GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)
                                   * int(baby_d[search_lst[i]][str(YEARS[j])]) / 1000,
                                   text=str(search_lst[i]) + str(baby_d[search_lst[i]][str(YEARS[j])]),
                                   anchor=tkinter.SW, fill=str(COLORS[i % len(COLORS)]))
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j+1) + TEXT_DX,
                                   GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)
                                   * int(baby_d[search_lst[i]][str(YEARS[j+1])]) / 1000,
                                   text=str(search_lst[i]) + str(baby_d[search_lst[i]][str(YEARS[j+1])]),
                                   anchor=tkinter.SW, fill=str(COLORS[i % len(COLORS)]))
            elif str(YEARS[j]) not in baby_d[search_lst[i]] and str(YEARS[j+1]) not in baby_d[search_lst[i]]:
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j),
                                   GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE),
                                   get_x_coordinate(CANVAS_WIDTH, j + 1),
                                   GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE), width=LINE_WIDTH,
                                   fill=str(COLORS[i % len(COLORS)]))
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX,
                                   CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                   text=str(search_lst[i]) + str('*'),
                                   anchor=tkinter.SW, fill=str(COLORS[i % len(COLORS)]))
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j + 1) + TEXT_DX,
                                   CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                   text=str(search_lst[i]) + str('*'),
                                   anchor=tkinter.SW, fill=str(COLORS[i % len(COLORS)]))

            elif str(YEARS[j]) in baby_d[search_lst[i]] and \
                    str(YEARS[j+1]) not in baby_d[search_lst[i]]:
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j),
                                   GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)
                                   * int(baby_d[search_lst[i]][str(YEARS[j])]) / 1000,
                                   get_x_coordinate(CANVAS_WIDTH, j + 1),
                                   GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE), width=LINE_WIDTH,
                                   fill=str(COLORS[i % len(COLORS)]))
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX,
                                   GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)
                                   * int(baby_d[search_lst[i]][str(YEARS[j])]) / 1000,
                                   text=str(search_lst[i]) + str(baby_d[search_lst[i]][str(YEARS[j])]),
                                   anchor=tkinter.SW, fill=str(COLORS[i % len(COLORS)]))
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j+1) + TEXT_DX,
                                   CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                   text=str(search_lst[i]) + str('*'),
                                   anchor=tkinter.SW, fill=str(COLORS[i % len(COLORS)]))
            elif str(YEARS[j+1]) in baby_d[search_lst[i]] and \
                    str(YEARS[j]) not in baby_d[search_lst[i]]:
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j),
                                   GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE),
                                   get_x_coordinate(CANVAS_WIDTH, j + 1),
                                   GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)
                                   * int(baby_d[search_lst[i]][str(YEARS[j + 1])]) / 1000, width=LINE_WIDTH,
                                   fill=str(COLORS[i % len(COLORS)]))
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX,
                                   CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                   text=str(search_lst[i]) + str('*'),
                                   anchor=tkinter.SW, fill=str(COLORS[i % len(COLORS)]))
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j+1) + TEXT_DX,
                                   GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)
                                   * int(baby_d[search_lst[i]][str(YEARS[j+1])]) / 1000,
                                   text=str(search_lst[i]) + str(baby_d[search_lst[i]][str(YEARS[j+1])]),
                                   anchor=tkinter.SW, fill=str(COLORS[i % len(COLORS)]))


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
