"""PuzzleMadness Arrow Sudoku — 2025-11-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 3)], [(6, 4), (6, 5), (5, 6)])
    puzzle.add_arrow([(4, 3)], [(3, 4), (4, 4)])
    puzzle.add_arrow([(1, 8)], [(2, 8), (3, 7)])
    puzzle.add_arrow([(6, 1)], [(6, 0), (5, 1), (5, 2), (4, 1)])
    puzzle.add_arrow([(1, 6)], [(2, 7), (2, 6), (3, 5)])
    puzzle.add_arrow([(1, 5)], [(2, 4), (3, 3)])
    puzzle.add_arrow([(6, 7)], [(7, 7), (7, 6), (8, 5)])
    puzzle.add_arrow([(0, 3)], [(0, 2), (1, 2), (1, 3), (1, 4)])
    puzzle.add_arrow([(0, 1)], [(1, 1), (2, 0)])
    puzzle.add_arrow([(7, 0)], [(8, 1), (7, 2), (8, 2)])
    puzzle.add_arrow([(8, 7)], [(7, 8), (8, 8)])
    puzzle.add_arrow([(4, 7)], [(4, 8), (3, 8)])
    puzzle.add_arrow([(6, 6)], [(5, 7), (6, 8)])
    puzzle.add_arrow([(2, 5)], [(3, 6), (4, 6)])

    return puzzle
