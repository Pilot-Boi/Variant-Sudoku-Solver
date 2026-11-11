"""PuzzleMadness Arrow Sudoku — 2025-05-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-05-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/5/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 2)], [(2, 3), (3, 3)])
    puzzle.add_arrow([(6, 5)], [(5, 4), (6, 3), (7, 2), (7, 1)])
    puzzle.add_arrow([(3, 7)], [(2, 7), (3, 6), (4, 6)])
    puzzle.add_arrow([(1, 4)], [(1, 5), (0, 5), (1, 6), (2, 6)])
    puzzle.add_arrow([(8, 6)], [(7, 6), (8, 7)])
    puzzle.add_arrow([(8, 5)], [(7, 4), (7, 5)])
    puzzle.add_arrow([(6, 6)], [(5, 5), (5, 6)])
    puzzle.add_arrow([(0, 1)], [(0, 2), (1, 1), (1, 0)])
    puzzle.add_arrow([(5, 7)], [(4, 8), (4, 7)])
    puzzle.add_arrow([(8, 0)], [(8, 1), (8, 2)])
    puzzle.add_arrow([(4, 3)], [(5, 3), (6, 2)])
    puzzle.add_arrow([(3, 1)], [(4, 1), (5, 0)])
    puzzle.add_arrow([(2, 0)], [(3, 0), (4, 0)])
    puzzle.add_arrow([(2, 8)], [(1, 7), (0, 7)])
    puzzle.add_arrow([(2, 5)], [(2, 4), (3, 4)])
    puzzle.add_arrow([(7, 8)], [(6, 7), (6, 8)])

    return puzzle
