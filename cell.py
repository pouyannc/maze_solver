from graphics import *

class Cell:
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.visited = False
        self._win = window

    def draw(self, x1, x2, y1, y2):
        if self._win is None:
            return

        fill_color = "black"

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        ptl = Point(self._x1, self._y1)
        ptr = Point(self._x2, self._y1)
        pbl = Point(self._x1, self._y2)
        pbr = Point(self._x2, self._y2)

        self._win.draw_line(Line(ptl, pbl), fill_color)
        self._win.draw_line(Line(ptr, pbr), fill_color)
        self._win.draw_line(Line(ptl, ptr), fill_color)
        self._win.draw_line(Line(pbl, pbr), fill_color)

        if not self.has_left_wall:
            self._win.draw_line(Line(ptl, pbl), "white")
        if not self.has_right_wall:
            self._win.draw_line(Line(ptr, pbr), "white")
        if not self.has_top_wall:
            self._win.draw_line(Line(ptl, ptr), "white")
        if not self.has_bottom_wall:
            self._win.draw_line(Line(pbl, pbr), "white")
    
    def draw_move(self, to_cell, undo=False):
        p1x = (self._x1 + self._x2) / 2
        p1y = (self._y1 + self._y2) / 2
        p2x = (to_cell._x1 + to_cell._x2) / 2
        p2y = (to_cell._y1 + to_cell._y2) / 2

        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"

        self._win.draw_line(Line(Point(p1x, p1y), Point(p2x, p2y)), fill_color)
