"""PuzzleMadness Arrow Sudoku — 2025-11-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 0, 7],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 6, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 2)], [(2, 3), (3, 3), (4, 2), (3, 1)])
    puzzle.add_arrow([(2, 4)], [(1, 5), (1, 6)])
    puzzle.add_arrow([(7, 2)], [(6, 2), (6, 1), (7, 1)])
    puzzle.add_arrow([(6, 6)], [(5, 6), (4, 7)])
    puzzle.add_arrow([(0, 1)], [(0, 0), (1, 0)])
    puzzle.add_arrow([(7, 6)], [(8, 7), (8, 6), (7, 5), (8, 5)])
    puzzle.add_arrow([(5, 0)], [(4, 1), (5, 2)])
    puzzle.add_arrow([(0, 2)], [(1, 2), (2, 1)])
    puzzle.add_arrow([(5, 8)], [(4, 8), (5, 7)])
    puzzle.add_arrow([(0, 5)], [(0, 4), (1, 3), (0, 3)])
    puzzle.add_arrow([(2, 5)], [(3, 6), (2, 6), (2, 7)])
    puzzle.add_arrow([(6, 8)], [(6, 7), (7, 8)])
    puzzle.add_arrow([(7, 3)], [(7, 4), (6, 5)])
    puzzle.add_arrow([(5, 3)], [(4, 3), (3, 4)])
    puzzle.add_arrow([(4, 4)], [(5, 5), (4, 5)])
    puzzle.add_arrow([(8, 1)], [(7, 0), (6, 0)])

    return puzzle
