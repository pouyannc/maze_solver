from window import Window
from graphics import *
from cell import Cell

def main():
    win = Window(800, 600)
    c1 = Cell(40,80,40,80,win,has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True)
    c2 = Cell(100,180,100,180,win,has_left_wall=False, has_right_wall=False, has_top_wall=True, has_bottom_wall=True)
    c3 = Cell(240,280,240,280,win,has_left_wall=False, has_right_wall=True, has_top_wall=True, has_bottom_wall=False)
    c4 = Cell(340,380,340,380,win,has_left_wall=False, has_right_wall=False, has_top_wall=False, has_bottom_wall=True)
    c1.draw()
    c2.draw()
    c3.draw()
    c4.draw()
    c1.draw_move(c2, undo=True)
    win.wait_for_close()

if __name__ == "__main__":
    main()