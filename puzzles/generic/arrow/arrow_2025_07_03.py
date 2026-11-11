"""PuzzleMadness Arrow Sudoku — 2025-07-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-07-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/7/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [5, 0, 4, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 6)], [(3, 5), (3, 6)])
    puzzle.add_arrow([(6, 3)], [(6, 2), (7, 3)])
    puzzle.add_arrow([(1, 5)], [(0, 4), (1, 3)])
    puzzle.add_arrow([(6, 7)], [(6, 6), (5, 6), (4, 5)])
    puzzle.add_arrow([(0, 0)], [(1, 0), (1, 1), (2, 2)])
    puzzle.add_arrow([(0, 8)], [(0, 7), (0, 6)])
    puzzle.add_arrow([(4, 2)], [(3, 3), (4, 3)])
    puzzle.add_arrow([(7, 1)], [(6, 1), (7, 2)])
    puzzle.add_arrow([(0, 2)], [(1, 2), (2, 1), (3, 0)])
    puzzle.add_arrow([(3, 4)], [(2, 3), (2, 4)])
    puzzle.add_arrow([(4, 4)], [(5, 4), (6, 4)])
    puzzle.add_arrow([(7, 5)], [(7, 6), (6, 5), (7, 4)])
    puzzle.add_arrow([(4, 8)], [(4, 7), (3, 7), (2, 7)])
    puzzle.add_arrow([(1, 4)], [(0, 5), (1, 6)])
    puzzle.add_arrow([(3, 1)], [(4, 1), (5, 0), (4, 0)])
    puzzle.add_arrow([(7, 7)], [(7, 8), (6, 8)])
    puzzle.add_arrow([(8, 0)], [(8, 1), (7, 0)])

    return puzzle
