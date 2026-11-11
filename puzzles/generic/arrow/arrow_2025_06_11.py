"""PuzzleMadness Arrow Sudoku — 2025-06-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-06-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/6/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 2, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 2)], [(7, 1), (6, 1), (6, 2), (5, 3)])
    puzzle.add_arrow([(5, 0)], [(4, 1), (3, 2)])
    puzzle.add_arrow([(1, 3)], [(0, 4), (1, 4), (2, 4)])
    puzzle.add_arrow([(7, 4)], [(7, 5), (8, 5), (8, 6), (7, 6)])
    puzzle.add_arrow([(6, 7)], [(5, 7), (6, 8)])
    puzzle.add_arrow([(0, 8)], [(1, 8), (0, 7)])
    puzzle.add_arrow([(4, 6)], [(4, 7), (4, 8)])
    puzzle.add_arrow([(2, 6)], [(3, 6), (2, 7)])
    puzzle.add_arrow([(3, 1)], [(4, 0), (3, 0)])
    puzzle.add_arrow([(1, 1)], [(1, 0), (2, 0)])
    puzzle.add_arrow([(3, 4)], [(3, 3), (2, 3)])
    puzzle.add_arrow([(6, 4)], [(7, 3), (8, 4)])
    puzzle.add_arrow([(1, 7)], [(1, 6), (2, 5)])
    puzzle.add_arrow([(4, 4)], [(4, 5), (5, 4)])
    puzzle.add_arrow([(5, 5)], [(6, 5), (5, 6)])
    puzzle.add_arrow([(8, 8)], [(7, 7), (7, 8)])

    return puzzle
