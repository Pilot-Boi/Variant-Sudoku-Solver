"""PuzzleMadness Arrow Sudoku — 2025-07-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-07-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/7/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 5)], [(7, 6), (8, 6)])
    puzzle.add_arrow([(4, 4)], [(4, 5), (5, 5), (5, 6), (6, 7), (5, 8)])
    puzzle.add_arrow([(1, 5)], [(2, 5), (1, 4)])
    puzzle.add_arrow([(7, 3)], [(6, 2), (7, 1), (7, 0)])
    puzzle.add_arrow([(2, 0)], [(3, 1), (2, 1), (1, 2), (1, 3), (0, 3)])
    puzzle.add_arrow([(2, 7)], [(2, 6), (1, 7), (2, 8)])
    puzzle.add_arrow([(4, 8)], [(4, 7), (5, 7)])
    puzzle.add_arrow([(6, 0)], [(6, 1), (5, 2)])
    puzzle.add_arrow([(5, 1)], [(4, 1), (5, 0)])
    puzzle.add_arrow([(8, 1)], [(7, 2), (8, 3)])
    puzzle.add_arrow([(5, 3)], [(6, 3), (7, 4)])
    puzzle.add_arrow([(1, 6)], [(0, 7), (0, 8)])
    puzzle.add_arrow([(4, 6)], [(3, 6), (3, 5)])
    puzzle.add_arrow([(3, 2)], [(4, 2), (4, 3)])
    puzzle.add_arrow([(0, 0)], [(0, 1), (0, 2)])
    puzzle.add_arrow([(7, 7)], [(6, 6), (7, 5)])
    puzzle.add_arrow([(2, 2)], [(2, 3), (2, 4)])

    return puzzle
