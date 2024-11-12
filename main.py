from window import Window
from graphics import *
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    new_maze = Maze(40, 40, 8, 8, 40, 40, win)
    new_maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()