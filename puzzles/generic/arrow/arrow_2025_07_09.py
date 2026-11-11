"""PuzzleMadness Arrow Sudoku — 2025-07-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-07-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/7/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 8, 2, 0, 4, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 3)], [(1, 4), (0, 4), (1, 5)])
    puzzle.add_arrow([(6, 2)], [(5, 3), (4, 3), (5, 2)])
    puzzle.add_arrow([(2, 6)], [(1, 7), (1, 6)])
    puzzle.add_arrow([(2, 1)], [(2, 0), (1, 0)])
    puzzle.add_arrow([(7, 6)], [(6, 7), (7, 7), (8, 8)])
    puzzle.add_arrow([(4, 7)], [(5, 7), (4, 6), (4, 5)])
    puzzle.add_arrow([(4, 2)], [(4, 1), (3, 1), (2, 2)])
    puzzle.add_arrow([(6, 1)], [(7, 0), (8, 1), (7, 2)])
    puzzle.add_arrow([(7, 4)], [(6, 5), (7, 5)])
    puzzle.add_arrow([(1, 2)], [(2, 3), (3, 2)])
    puzzle.add_arrow([(3, 7)], [(3, 8), (2, 7)])
    puzzle.add_arrow([(4, 0)], [(5, 1), (6, 0)])
    puzzle.add_arrow([(8, 2)], [(7, 3), (8, 4)])
    puzzle.add_arrow([(3, 5)], [(2, 4), (3, 3)])

    return puzzle
