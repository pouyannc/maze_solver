import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 4
        num_rows = 6
        m1 = Maze(0, 0, num_rows, num_cols, 40, 40)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 40, 40)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_exit(self):
        num_cols = 4
        num_rows = 6
        m1 = Maze(0, 0, num_rows, num_cols, 40, 40)
        self.assertFalse(
            m1._cells[0][0].has_top_wall
        )
        self.assertFalse(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall
        )
    
    def test_maze_reset_cells_visited(self):
        num_cols = 4
        num_rows = 6
        m1 = Maze(0, 0, num_rows, num_cols, 40, 40, seed=0)
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertFalse(
                    m1._cells[i][j].visited
                )

if __name__ == "__main__":
    unittest.main()