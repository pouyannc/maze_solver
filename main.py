from window import Window
from graphics import *

def main():
    win = Window(800, 600)
    line1 = Line(Point(8,8), Point(300,300))
    win.draw_line(line1, "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()