"""PuzzleMadness Arrow Sudoku — 2025-02-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 5, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 0)], [(6, 1), (7, 0)])
    puzzle.add_arrow([(3, 6)], [(3, 7), (2, 8), (2, 7)])
    puzzle.add_arrow([(7, 7)], [(6, 6), (6, 5), (7, 4)])
    puzzle.add_arrow([(4, 4)], [(4, 5), (5, 5), (6, 4), (7, 3)])
    puzzle.add_arrow([(2, 2)], [(1, 3), (1, 4)])
    puzzle.add_arrow([(4, 0)], [(3, 1), (2, 0)])
    puzzle.add_arrow([(0, 4)], [(0, 5), (1, 6), (1, 7), (0, 7)])
    puzzle.add_arrow([(3, 0)], [(4, 1), (3, 2), (4, 2)])
    puzzle.add_arrow([(6, 7)], [(5, 7), (4, 6)])
    puzzle.add_arrow([(7, 1)], [(6, 2), (5, 3)])
    puzzle.add_arrow([(0, 0)], [(1, 1), (0, 1)])
    puzzle.add_arrow([(8, 7)], [(8, 8), (7, 8)])
    puzzle.add_arrow([(4, 3)], [(3, 4), (2, 3)])
    puzzle.add_arrow([(6, 3)], [(5, 2), (5, 1)])
    puzzle.add_arrow([(8, 4)], [(8, 5), (8, 6)])

    return puzzle
