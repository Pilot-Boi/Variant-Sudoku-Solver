"""PuzzleMadness Arrow Sudoku — 2025-09-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [4, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 5)], [(2, 5), (1, 6), (1, 7)])
    puzzle.add_arrow([(7, 3)], [(8, 3), (7, 2)])
    puzzle.add_arrow([(4, 1)], [(5, 0), (4, 0)])
    puzzle.add_arrow([(1, 2)], [(2, 3), (3, 3), (3, 4)])
    puzzle.add_arrow([(5, 2)], [(4, 2), (5, 3), (5, 4), (6, 4)])
    puzzle.add_arrow([(4, 8)], [(3, 8), (4, 7), (3, 6)])
    puzzle.add_arrow([(8, 6)], [(7, 7), (6, 6), (7, 5), (8, 5)])
    puzzle.add_arrow([(1, 1)], [(0, 2), (0, 3)])
    puzzle.add_arrow([(2, 4)], [(1, 3), (1, 4)])
    puzzle.add_arrow([(7, 0)], [(6, 0), (7, 1)])
    puzzle.add_arrow([(6, 7)], [(7, 8), (6, 8)])
    puzzle.add_arrow([(2, 8)], [(2, 7), (2, 6)])
    puzzle.add_arrow([(6, 3)], [(7, 4), (6, 5)])
    puzzle.add_arrow([(3, 1)], [(2, 1), (2, 2)])

    return puzzle
