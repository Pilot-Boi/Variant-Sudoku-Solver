"""PuzzleMadness Arrow Sudoku — 2025-02-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 7)], [(3, 6), (2, 6), (1, 5)])
    puzzle.add_arrow([(4, 3)], [(3, 4), (3, 3), (4, 4)])
    puzzle.add_arrow([(6, 6)], [(6, 5), (6, 4), (5, 4)])
    puzzle.add_arrow([(1, 8)], [(2, 8), (3, 7)])
    puzzle.add_arrow([(4, 2)], [(5, 1), (6, 0)])
    puzzle.add_arrow([(6, 8)], [(6, 7), (7, 8), (8, 7)])
    puzzle.add_arrow([(2, 0)], [(1, 1), (1, 2), (0, 3)])
    puzzle.add_arrow([(6, 2)], [(6, 1), (7, 0)])
    puzzle.add_arrow([(4, 1)], [(5, 2), (6, 3)])
    puzzle.add_arrow([(7, 2)], [(8, 1), (8, 0), (7, 1)])
    puzzle.add_arrow([(1, 7)], [(1, 6), (0, 6)])
    puzzle.add_arrow([(5, 7)], [(5, 6), (4, 7)])
    puzzle.add_arrow([(1, 4)], [(2, 3), (2, 2), (3, 2)])
    puzzle.add_arrow([(4, 5)], [(5, 5), (4, 6)])
    puzzle.add_arrow([(8, 6)], [(7, 7), (8, 8)])
    puzzle.add_arrow([(1, 0)], [(0, 1), (0, 0)])

    return puzzle
