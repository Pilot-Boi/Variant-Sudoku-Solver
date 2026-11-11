"""PuzzleMadness Arrow Sudoku — 2025-10-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 3)], [(5, 2), (4, 3), (3, 4), (2, 5)])
    puzzle.add_arrow([(1, 3)], [(2, 2), (3, 3)])
    puzzle.add_arrow([(5, 7)], [(4, 7), (4, 6), (3, 6)])
    puzzle.add_arrow([(8, 8)], [(7, 7), (8, 6), (7, 5)])
    puzzle.add_arrow([(0, 2)], [(1, 1), (1, 2), (0, 1)])
    puzzle.add_arrow([(1, 7)], [(1, 8), (2, 8)])
    puzzle.add_arrow([(6, 2)], [(7, 3), (6, 4), (5, 5)])
    puzzle.add_arrow([(3, 2)], [(4, 2), (4, 1)])
    puzzle.add_arrow([(4, 0)], [(5, 1), (6, 0), (7, 0)])
    puzzle.add_arrow([(0, 5)], [(0, 4), (1, 4)])
    puzzle.add_arrow([(6, 5)], [(6, 6), (7, 6)])
    puzzle.add_arrow([(8, 3)], [(7, 4), (8, 5)])
    puzzle.add_arrow([(7, 1)], [(8, 1), (8, 0)])
    puzzle.add_arrow([(7, 8)], [(6, 7), (5, 8)])

    return puzzle
