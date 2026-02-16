from array_adt import Array
import time
import os


class GameOfLife:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = Array(rows)

        for i in range(rows):
            self.grid[i] = Array(cols)
            for j in range(cols):
                self.grid[i][j] = 0

    def set_alive(self, row, col):
        self.grid[row][col] = 1

    def count_neighbors(self, row, col):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        count = 0
        for dr, dc in directions:
            r = row + dr
            c = col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                count += self.grid[r][c]

        return count

    def next_generation(self):
        new_grid = Array(self.rows)

        for i in range(self.rows):
            new_grid[i] = Array(self.cols)
            for j in range(self.cols):

                alive = self.grid[i][j]
                neighbors = self.count_neighbors(i, j)

                if alive == 1:
                    if neighbors == 2 or neighbors == 3:
                        new_grid[i][j] = 1
                    else:
                        new_grid[i][j] = 0
                else:
                    if neighbors == 3:
                        new_grid[i][j] = 1
                    else:
                        new_grid[i][j] = 0

        self.grid = new_grid

    def display(self):
        os.system("cls" if os.name == "nt" else "clear")
        for i in range(self.rows):
            row_str = ""
            for j in range(self.cols):
                if self.grid[i][j] == 1:
                    row_str += "■ "
                else:
                    row_str += ". "
            print(row_str)
