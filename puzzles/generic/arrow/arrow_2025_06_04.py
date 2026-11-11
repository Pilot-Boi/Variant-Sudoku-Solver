"""PuzzleMadness Arrow Sudoku — 2025-06-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-06-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/6/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 3, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 3, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 3)], [(1, 2), (2, 3), (3, 3), (2, 4), (3, 5)])
    puzzle.add_arrow([(5, 4)], [(6, 3), (5, 2), (6, 2)])
    puzzle.add_arrow([(5, 8)], [(6, 7), (7, 7)])
    puzzle.add_arrow([(6, 4)], [(7, 4), (8, 4)])
    puzzle.add_arrow([(5, 1)], [(5, 0), (6, 0), (7, 1)])
    puzzle.add_arrow([(6, 6)], [(5, 7), (5, 6)])
    puzzle.add_arrow([(1, 7)], [(1, 6), (0, 5)])
    puzzle.add_arrow([(4, 7)], [(4, 8), (3, 7)])
    puzzle.add_arrow([(2, 1)], [(2, 2), (3, 1)])
    puzzle.add_arrow([(8, 5)], [(7, 5), (8, 6)])
    puzzle.add_arrow([(3, 8)], [(2, 8), (1, 8), (0, 8)])
    puzzle.add_arrow([(4, 4)], [(5, 3), (4, 2)])
    puzzle.add_arrow([(4, 5)], [(4, 6), (5, 5)])
    puzzle.add_arrow([(7, 8)], [(8, 7), (8, 8)])
    puzzle.add_arrow([(1, 0)], [(0, 0), (0, 1)])
    puzzle.add_arrow([(1, 5)], [(1, 4), (0, 3)])
    puzzle.add_arrow([(7, 0)], [(8, 1), (8, 2)])

    return puzzle
