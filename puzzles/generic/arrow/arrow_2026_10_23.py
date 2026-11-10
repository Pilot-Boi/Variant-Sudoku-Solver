"""PuzzleMadness Arrow Sudoku — 2026-10-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2026-10-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2026/10/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 7)], [(4, 6), (5, 6), (4, 5), (3, 5)])
    puzzle.add_arrow([(1, 1)], [(0, 2), (1, 3), (2, 4)])
    puzzle.add_arrow([(5, 0)], [(6, 1), (5, 1), (6, 2), (5, 2)])
    puzzle.add_arrow([(3, 2)], [(2, 1), (3, 1)])
    puzzle.add_arrow([(3, 7)], [(2, 8), (1, 7)])
    puzzle.add_arrow([(7, 2)], [(8, 2), (7, 1)])
    puzzle.add_arrow([(7, 6)], [(7, 5), (6, 6), (6, 7), (7, 7)])
    puzzle.add_arrow([(4, 3)], [(4, 4), (5, 3)])
    puzzle.add_arrow([(8, 7)], [(8, 8), (7, 8)])
    puzzle.add_arrow([(4, 8)], [(4, 7), (3, 6)])
    puzzle.add_arrow([(0, 6)], [(0, 7), (1, 8)])
    puzzle.add_arrow([(2, 5)], [(1, 4), (0, 4)])
    puzzle.add_arrow([(8, 4)], [(8, 3), (7, 4), (6, 4)])
    puzzle.add_arrow([(3, 0)], [(4, 1), (4, 2)])
    puzzle.add_arrow([(2, 0)], [(1, 0), (0, 0)])
    puzzle.add_arrow([(6, 0)], [(7, 0), (8, 0)])
    puzzle.add_arrow([(1, 2)], [(2, 3), (3, 3)])

    return puzzle
