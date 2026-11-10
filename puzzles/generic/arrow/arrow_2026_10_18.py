"""PuzzleMadness Arrow Sudoku — 2026-10-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2026-10-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2026/10/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [5, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 5)], [(6, 5), (7, 5)])
    puzzle.add_arrow([(1, 2)], [(0, 3), (1, 3), (0, 4)])
    puzzle.add_arrow([(7, 2)], [(8, 1), (7, 1), (8, 2)])
    puzzle.add_arrow([(0, 7)], [(1, 6), (2, 7), (3, 8)])
    puzzle.add_arrow([(6, 3)], [(5, 2), (4, 1)])
    puzzle.add_arrow([(6, 2)], [(6, 1), (5, 0)])
    puzzle.add_arrow([(6, 8)], [(7, 7), (7, 8), (8, 8)])
    puzzle.add_arrow([(6, 7)], [(6, 6), (7, 6)])
    puzzle.add_arrow([(5, 3)], [(4, 2), (3, 3), (2, 2)])
    puzzle.add_arrow([(0, 2)], [(1, 1), (0, 0)])
    puzzle.add_arrow([(4, 6)], [(3, 5), (3, 4), (4, 4)])
    puzzle.add_arrow([(2, 5)], [(2, 6), (1, 7)])
    puzzle.add_arrow([(4, 8)], [(5, 7), (5, 6)])
    puzzle.add_arrow([(3, 0)], [(3, 1), (2, 0)])
    puzzle.add_arrow([(8, 3)], [(8, 4), (7, 3)])
    puzzle.add_arrow([(5, 4)], [(4, 3), (3, 2)])
    puzzle.add_arrow([(1, 5)], [(0, 5), (1, 4)])

    return puzzle
