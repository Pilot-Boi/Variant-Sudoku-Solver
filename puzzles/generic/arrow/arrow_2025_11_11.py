"""PuzzleMadness Arrow Sudoku — 2025-11-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 5, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(0, 1)], [(1, 1), (1, 2), (0, 3)])
    puzzle.add_arrow([(4, 5)], [(4, 6), (5, 5), (6, 5), (5, 4)])
    puzzle.add_arrow([(2, 2)], [(2, 3), (3, 2)])
    puzzle.add_arrow([(6, 6)], [(7, 6), (8, 5)])
    puzzle.add_arrow([(2, 1)], [(3, 1), (3, 0)])
    puzzle.add_arrow([(4, 2)], [(5, 2), (5, 3), (6, 2)])
    puzzle.add_arrow([(5, 6)], [(4, 7), (4, 8)])
    puzzle.add_arrow([(8, 2)], [(7, 2), (7, 3), (8, 4)])
    puzzle.add_arrow([(0, 4)], [(1, 5), (0, 5), (1, 6)])
    puzzle.add_arrow([(6, 7)], [(7, 7), (8, 7), (7, 8)])
    puzzle.add_arrow([(3, 6)], [(2, 7), (3, 7)])
    puzzle.add_arrow([(7, 0)], [(6, 1), (6, 0)])
    puzzle.add_arrow([(3, 5)], [(3, 4), (4, 4)])
    puzzle.add_arrow([(1, 8)], [(1, 7), (2, 8)])
    puzzle.add_arrow([(2, 5)], [(1, 4), (1, 3)])

    return puzzle
