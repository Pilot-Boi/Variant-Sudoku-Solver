"""PuzzleMadness Arrow Sudoku — 2025-04-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 4, 0, 0, 0, 0],
        [6, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 3)], [(4, 4), (5, 4)])
    puzzle.add_arrow([(7, 2)], [(6, 3), (6, 2)])
    puzzle.add_arrow([(6, 5)], [(6, 4), (5, 5), (6, 6)])
    puzzle.add_arrow([(4, 2)], [(3, 1), (4, 1), (4, 0)])
    puzzle.add_arrow([(1, 4)], [(1, 5), (1, 6)])
    puzzle.add_arrow([(4, 7)], [(4, 6), (3, 6)])
    puzzle.add_arrow([(7, 1)], [(6, 0), (7, 0)])
    puzzle.add_arrow([(1, 1)], [(2, 2), (3, 2), (2, 3)])
    puzzle.add_arrow([(0, 1)], [(1, 2), (0, 3)])
    puzzle.add_arrow([(7, 6)], [(7, 7), (7, 8)])
    puzzle.add_arrow([(6, 8)], [(5, 7), (5, 8)])
    puzzle.add_arrow([(8, 2)], [(8, 3), (8, 4)])
    puzzle.add_arrow([(7, 3)], [(7, 4), (8, 5)])
    puzzle.add_arrow([(2, 6)], [(1, 7), (0, 6)])
    puzzle.add_arrow([(2, 7)], [(2, 8), (3, 7)])
    puzzle.add_arrow([(0, 4)], [(1, 3), (0, 2)])
    puzzle.add_arrow([(5, 0)], [(6, 1), (5, 1)])

    return puzzle
