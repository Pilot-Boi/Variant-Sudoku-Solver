"""PuzzleMadness Arrow Sudoku — 2026-10-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2026-10-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2026/10/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 4],
        [0, 0, 5, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 5)], [(4, 6), (3, 5), (2, 5)])
    puzzle.add_arrow([(0, 1)], [(0, 2), (1, 2)])
    puzzle.add_arrow([(5, 2)], [(5, 3), (6, 4), (6, 3)])
    puzzle.add_arrow([(3, 7)], [(3, 8), (4, 7), (3, 6), (2, 7)])
    puzzle.add_arrow([(3, 1)], [(4, 0), (5, 0), (6, 0)])
    puzzle.add_arrow([(2, 3)], [(2, 2), (1, 3), (0, 4)])
    puzzle.add_arrow([(7, 5)], [(6, 5), (7, 4)])
    puzzle.add_arrow([(6, 8)], [(7, 8), (8, 7), (8, 8)])
    puzzle.add_arrow([(7, 3)], [(7, 2), (7, 1), (8, 2)])
    puzzle.add_arrow([(8, 5)], [(8, 6), (7, 6)])
    puzzle.add_arrow([(4, 3)], [(5, 4), (4, 4)])
    puzzle.add_arrow([(0, 8)], [(0, 7), (1, 8)])
    puzzle.add_arrow([(2, 1)], [(1, 1), (2, 0)])
    puzzle.add_arrow([(4, 2)], [(5, 1), (4, 1)])
    puzzle.add_arrow([(2, 6)], [(1, 7), (1, 6)])

    return puzzle
