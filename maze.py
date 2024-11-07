from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
    
    def _create_cells(self):
        self._cells = [[Cell(self._win) for j in range(self._num_rows)] for i in range(self._num_cols)]
    
    def _draw_cell(self, i, j):
        # i is col, j is row
        px1 = self._x1 + (self._cell_size_x * i)
        py1 = self._y1 + (self._cell_size_y * j)
        px2 = px1 + self._cell_size_x
        py2 = py1 + self._cell_size_y

        self._cells[i][j].draw(px1, px2, py1, py2)

        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.5)
