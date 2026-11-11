"""PuzzleMadness Arrow Sudoku — 2025-02-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 0, 6, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 0)], [(7, 0), (6, 1), (7, 2), (8, 3)])
    puzzle.add_arrow([(7, 4)], [(6, 3), (6, 4)])
    puzzle.add_arrow([(5, 8)], [(6, 7), (6, 8)])
    puzzle.add_arrow([(2, 4)], [(1, 4), (1, 3)])
    puzzle.add_arrow([(1, 0)], [(1, 1), (0, 1)])
    puzzle.add_arrow([(5, 2)], [(4, 3), (4, 2)])
    puzzle.add_arrow([(5, 3)], [(4, 4), (5, 5), (4, 6), (3, 5)])
    puzzle.add_arrow([(4, 1)], [(3, 2), (3, 1), (2, 0)])
    puzzle.add_arrow([(5, 1)], [(5, 0), (4, 0)])
    puzzle.add_arrow([(2, 6)], [(1, 5), (1, 6)])
    puzzle.add_arrow([(1, 8)], [(2, 8), (1, 7), (0, 7)])
    puzzle.add_arrow([(2, 3)], [(2, 2), (3, 3)])
    puzzle.add_arrow([(4, 7)], [(4, 8), (5, 7)])
    puzzle.add_arrow([(8, 1)], [(7, 1), (6, 2)])
    puzzle.add_arrow([(8, 6)], [(8, 7), (7, 6)])
    puzzle.add_arrow([(1, 2)], [(0, 3), (0, 4)])
    puzzle.add_arrow([(6, 6)], [(7, 7), (8, 8)])

    return puzzle
