"""PuzzleMadness Arrow Sudoku — 2025-07-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-07-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/7/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 5, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 5)], [(6, 6), (5, 7)])
    puzzle.add_arrow([(0, 6)], [(1, 6), (1, 5)])
    puzzle.add_arrow([(1, 1)], [(2, 2), (2, 1), (1, 0)])
    puzzle.add_arrow([(3, 1)], [(4, 2), (3, 2)])
    puzzle.add_arrow([(6, 2)], [(7, 1), (7, 0)])
    puzzle.add_arrow([(7, 4)], [(8, 5), (7, 6)])
    puzzle.add_arrow([(2, 3)], [(2, 4), (3, 4)])
    puzzle.add_arrow([(4, 1)], [(5, 2), (6, 3)])
    puzzle.add_arrow([(5, 4)], [(5, 3), (4, 4)])
    puzzle.add_arrow([(2, 6)], [(1, 7), (1, 8), (2, 8)])
    puzzle.add_arrow([(4, 8)], [(3, 7), (3, 6)])
    puzzle.add_arrow([(0, 5)], [(1, 4), (0, 3)])
    puzzle.add_arrow([(1, 2)], [(0, 2), (0, 1)])
    puzzle.add_arrow([(7, 7)], [(8, 7), (8, 6)])
    puzzle.add_arrow([(5, 5)], [(5, 6), (6, 7)])
    puzzle.add_arrow([(7, 3)], [(7, 2), (8, 3)])
    puzzle.add_arrow([(8, 8)], [(7, 8), (6, 8)])
    puzzle.add_arrow([(5, 0)], [(4, 0), (3, 0)])

    return puzzle
