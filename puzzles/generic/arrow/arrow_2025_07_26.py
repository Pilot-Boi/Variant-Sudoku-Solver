"""PuzzleMadness Arrow Sudoku — 2025-07-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-07-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/7/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 6, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 2)], [(2, 3), (1, 3), (1, 4)])
    puzzle.add_arrow([(1, 7)], [(2, 7), (1, 6)])
    puzzle.add_arrow([(8, 4)], [(7, 5), (6, 5), (5, 6)])
    puzzle.add_arrow([(7, 3)], [(7, 2), (6, 2)])
    puzzle.add_arrow([(6, 3)], [(5, 3), (4, 2), (4, 3)])
    puzzle.add_arrow([(6, 7)], [(5, 8), (5, 7)])
    puzzle.add_arrow([(2, 5)], [(3, 5), (3, 6), (4, 5)])
    puzzle.add_arrow([(6, 6)], [(7, 6), (8, 7)])
    puzzle.add_arrow([(5, 0)], [(4, 1), (3, 0), (2, 0)])
    puzzle.add_arrow([(3, 1)], [(4, 0), (5, 1)])
    puzzle.add_arrow([(7, 7)], [(6, 8), (7, 8), (8, 8)])
    puzzle.add_arrow([(0, 1)], [(0, 0), (1, 0), (2, 1)])
    puzzle.add_arrow([(5, 2)], [(6, 1), (6, 0)])
    puzzle.add_arrow([(5, 4)], [(6, 4), (5, 5)])
    puzzle.add_arrow([(7, 1)], [(8, 2), (8, 3)])
    puzzle.add_arrow([(1, 5)], [(0, 5), (0, 6)])

    return puzzle
