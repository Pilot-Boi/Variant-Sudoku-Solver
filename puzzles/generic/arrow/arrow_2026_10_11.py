"""PuzzleMadness Arrow Sudoku — 2026-10-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2026-10-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2026/10/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 9, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 3)], [(6, 2), (7, 2), (7, 1)])
    puzzle.add_arrow([(4, 7)], [(4, 8), (5, 7)])
    puzzle.add_arrow([(3, 0)], [(2, 1), (3, 1)])
    puzzle.add_arrow([(0, 8)], [(1, 8), (2, 8), (2, 7)])
    puzzle.add_arrow([(8, 5)], [(8, 4), (7, 4)])
    puzzle.add_arrow([(5, 0)], [(4, 1), (5, 2)])
    puzzle.add_arrow([(0, 4)], [(1, 3), (2, 4)])
    puzzle.add_arrow([(6, 0)], [(7, 0), (8, 0)])
    puzzle.add_arrow([(7, 8)], [(8, 8), (8, 7)])
    puzzle.add_arrow([(1, 6)], [(2, 5), (1, 4)])
    puzzle.add_arrow([(4, 4)], [(4, 3), (3, 3)])
    puzzle.add_arrow([(5, 5)], [(4, 6), (5, 6), (6, 6)])
    puzzle.add_arrow([(6, 5)], [(7, 6), (6, 7)])
    puzzle.add_arrow([(2, 2)], [(1, 1), (1, 0), (2, 0)])
    puzzle.add_arrow([(7, 7)], [(6, 8), (5, 8)])
    puzzle.add_arrow([(1, 2)], [(0, 1), (0, 0)])
    puzzle.add_arrow([(8, 6)], [(7, 5), (6, 4), (5, 3)])
    puzzle.add_arrow([(1, 7)], [(0, 6), (1, 5), (0, 5)])
    puzzle.add_arrow([(3, 6)], [(4, 5), (3, 4)])
    puzzle.add_arrow([(8, 2)], [(8, 3), (7, 3)])

    return puzzle
