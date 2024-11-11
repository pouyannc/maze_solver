from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
    
    def _create_cells(self):
        self._cells = [[Cell(self._win) for j in range(self._num_rows)] for i in range(self._num_cols)]
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _draw_cell(self, i, j):
        # i is col, j is row
        px1 = self._x1 + (self._cell_size_x * i)
        py1 = self._y1 + (self._cell_size_y * j)
        px2 = px1 + self._cell_size_x
        py2 = py1 + self._cell_size_y

        self._cells[i][j].draw(px1, px2, py1, py2)

        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.5)
