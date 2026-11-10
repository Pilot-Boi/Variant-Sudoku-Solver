"""PuzzleMadness Arrow Sudoku — 2026-10-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2026-10-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2026/10/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 7)], [(4, 7), (5, 8), (6, 8)])
    puzzle.add_arrow([(6, 1)], [(5, 2), (5, 1), (5, 0)])
    puzzle.add_arrow([(2, 0)], [(2, 1), (1, 1), (1, 2)])
    puzzle.add_arrow([(0, 6)], [(0, 5), (1, 6), (0, 7)])
    puzzle.add_arrow([(1, 5)], [(2, 5), (3, 6), (3, 7)])
    puzzle.add_arrow([(7, 5)], [(8, 6), (8, 5)])
    puzzle.add_arrow([(7, 7)], [(8, 7), (8, 8)])
    puzzle.add_arrow([(7, 1)], [(6, 0), (7, 0)])
    puzzle.add_arrow([(2, 3)], [(1, 4), (0, 3)])
    puzzle.add_arrow([(3, 2)], [(4, 3), (3, 3), (3, 4)])
    puzzle.add_arrow([(5, 5)], [(6, 4), (7, 4)])
    puzzle.add_arrow([(7, 3)], [(6, 2), (7, 2)])
    puzzle.add_arrow([(4, 1)], [(4, 0), (3, 1)])
    puzzle.add_arrow([(6, 7)], [(5, 6), (6, 5)])
    puzzle.add_arrow([(5, 4)], [(4, 4), (4, 5)])
    puzzle.add_arrow([(0, 2)], [(1, 3), (2, 2)])

    return puzzle
