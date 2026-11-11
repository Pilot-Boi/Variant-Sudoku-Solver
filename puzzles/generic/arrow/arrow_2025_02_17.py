"""PuzzleMadness Arrow Sudoku — 2025-02-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 8, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 4)], [(6, 5), (5, 6)])
    puzzle.add_arrow([(1, 3)], [(2, 4), (3, 5), (3, 6)])
    puzzle.add_arrow([(2, 6)], [(2, 5), (1, 6)])
    puzzle.add_arrow([(6, 1)], [(5, 2), (4, 2), (4, 3)])
    puzzle.add_arrow([(2, 8)], [(2, 7), (3, 8)])
    puzzle.add_arrow([(5, 7)], [(6, 8), (7, 8)])
    puzzle.add_arrow([(5, 4)], [(5, 5), (6, 6)])
    puzzle.add_arrow([(2, 1)], [(2, 0), (1, 0), (0, 1)])
    puzzle.add_arrow([(5, 1)], [(4, 0), (4, 1)])
    puzzle.add_arrow([(1, 2)], [(2, 3), (1, 4), (0, 4)])
    puzzle.add_arrow([(8, 1)], [(7, 2), (7, 3)])
    puzzle.add_arrow([(7, 6)], [(8, 6), (7, 5), (6, 4)])
    puzzle.add_arrow([(8, 2)], [(7, 1), (6, 0)])
    puzzle.add_arrow([(7, 7)], [(6, 7), (5, 8)])
    puzzle.add_arrow([(0, 0)], [(1, 1), (2, 2)])

    return puzzle
