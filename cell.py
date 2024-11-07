from graphics import *

class Cell:
    def __init__(self, x1, x2, y1, y2, window, **kwargs):
        self.has_left_wall = kwargs['has_left_wall']
        self.has_right_wall = kwargs['has_right_wall']
        self.has_top_wall = kwargs['has_top_wall']
        self.has_bottom_wall = kwargs['has_bottom_wall']
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window

    def draw(self):
        fill_color = "black"

        ptl = Point(self._x1, self._y1)
        ptr = Point(self._x2, self._y1)
        pbl = Point(self._x1, self._y2)
        pbr = Point(self._x2, self._y2)

        if self.has_left_wall:
            self._win.draw_line(Line(ptl, pbl), fill_color)
        if self.has_right_wall:
            self._win.draw_line(Line(ptr, pbr), fill_color)
        if self.has_top_wall:
            self._win.draw_line(Line(ptl, ptr), fill_color)
        if self.has_bottom_wall:
            self._win.draw_line(Line(pbl, pbr), fill_color)
    
    def draw_move(self, to_cell, undo=False):
        p1x = (self._x1 + self._x2) / 2
        p1y = (self._y1 + self._y2) / 2
        p2x = (to_cell._x1 + to_cell._x2) / 2
        p2y = (to_cell._y1 + to_cell._y2) / 2

        if undo:
            fill_color = "red"
        else:
            fill_color = "gray"

        self._win.draw_line(Line(Point(p1x, p1y), Point(p2x, p2y)), fill_color)
