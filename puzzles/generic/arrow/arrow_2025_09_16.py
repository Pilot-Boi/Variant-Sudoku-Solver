"""PuzzleMadness Arrow Sudoku — 2025-09-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 3, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 7)], [(2, 6), (3, 7), (4, 6), (5, 6)])
    puzzle.add_arrow([(5, 1)], [(6, 1), (5, 0)])
    puzzle.add_arrow([(6, 6)], [(6, 5), (5, 4), (6, 3), (5, 2)])
    puzzle.add_arrow([(5, 3)], [(4, 4), (3, 3)])
    puzzle.add_arrow([(0, 4)], [(1, 5), (2, 4)])
    puzzle.add_arrow([(1, 3)], [(0, 2), (0, 3)])
    puzzle.add_arrow([(1, 6)], [(0, 6), (0, 5), (1, 4)])
    puzzle.add_arrow([(4, 0)], [(4, 1), (4, 2)])
    puzzle.add_arrow([(3, 1)], [(3, 0), (2, 1), (2, 2), (1, 2)])
    puzzle.add_arrow([(8, 1)], [(7, 1), (7, 0)])
    puzzle.add_arrow([(6, 2)], [(7, 3), (6, 4)])
    puzzle.add_arrow([(8, 4)], [(7, 5), (8, 6)])
    puzzle.add_arrow([(7, 7)], [(7, 8), (6, 8)])
    puzzle.add_arrow([(0, 8)], [(0, 7), (1, 8)])
    puzzle.add_arrow([(3, 4)], [(4, 3), (3, 2)])
    puzzle.add_arrow([(4, 8)], [(5, 8), (6, 7)])

    return puzzle
