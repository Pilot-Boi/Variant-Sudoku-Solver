"""PuzzleMadness Arrow Sudoku — 2025-07-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-07-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/7/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 8)], [(2, 7), (2, 6)])
    puzzle.add_arrow([(1, 4)], [(2, 4), (1, 5), (2, 5)])
    puzzle.add_arrow([(4, 2)], [(5, 1), (4, 0)])
    puzzle.add_arrow([(6, 2)], [(7, 3), (8, 2), (7, 2)])
    puzzle.add_arrow([(8, 7)], [(7, 8), (6, 7)])
    puzzle.add_arrow([(7, 5)], [(8, 5), (8, 4), (7, 4)])
    puzzle.add_arrow([(3, 6)], [(4, 6), (4, 7)])
    puzzle.add_arrow([(4, 3)], [(5, 4), (4, 4)])
    puzzle.add_arrow([(5, 6)], [(5, 7), (5, 8)])
    puzzle.add_arrow([(0, 1)], [(1, 2), (0, 2)])
    puzzle.add_arrow([(6, 6)], [(7, 6), (7, 7)])
    puzzle.add_arrow([(2, 0)], [(3, 1), (4, 1), (3, 2), (3, 3)])
    puzzle.add_arrow([(2, 1)], [(1, 1), (0, 0)])
    puzzle.add_arrow([(8, 1)], [(8, 0), (7, 1)])
    puzzle.add_arrow([(2, 3)], [(3, 4), (3, 5)])
    puzzle.add_arrow([(5, 2)], [(5, 3), (6, 3)])
    puzzle.add_arrow([(1, 6)], [(0, 6), (1, 7)])
    puzzle.add_arrow([(5, 0)], [(6, 0), (6, 1)])

    return puzzle
