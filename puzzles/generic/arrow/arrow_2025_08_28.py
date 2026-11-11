"""PuzzleMadness Arrow Sudoku — 2025-08-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-08-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/8/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 6, 0, 0, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 2)], [(4, 3), (3, 3)])
    puzzle.add_arrow([(2, 6)], [(3, 7), (2, 7), (3, 8)])
    puzzle.add_arrow([(4, 5)], [(4, 6), (5, 5), (5, 4)])
    puzzle.add_arrow([(3, 0)], [(2, 1), (1, 1), (2, 2)])
    puzzle.add_arrow([(7, 0)], [(6, 1), (5, 0), (6, 0)])
    puzzle.add_arrow([(2, 4)], [(3, 5), (4, 4)])
    puzzle.add_arrow([(7, 4)], [(8, 3), (7, 3), (7, 2)])
    puzzle.add_arrow([(8, 7)], [(8, 8), (7, 8)])
    puzzle.add_arrow([(1, 6)], [(1, 7), (0, 8)])
    puzzle.add_arrow([(1, 3)], [(0, 4), (1, 5), (1, 4)])
    puzzle.add_arrow([(8, 5)], [(8, 6), (7, 5)])
    puzzle.add_arrow([(6, 7)], [(7, 7), (7, 6)])
    puzzle.add_arrow([(5, 1)], [(4, 1), (3, 1), (3, 2)])
    puzzle.add_arrow([(0, 1)], [(1, 0), (2, 0)])
    puzzle.add_arrow([(4, 8)], [(5, 7), (5, 6)])
    puzzle.add_arrow([(6, 3)], [(6, 4), (6, 5)])
    puzzle.add_arrow([(0, 5)], [(0, 6), (0, 7)])

    return puzzle
