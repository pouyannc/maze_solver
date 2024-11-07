from window import Window
from graphics import *
from cell import Cell

def main():
    win = Window(800, 600)
    c1 = Cell(40,80,40,80,win,has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True)
    c1.draw()
    win.wait_for_close()

if __name__ == "__main__":
    main()