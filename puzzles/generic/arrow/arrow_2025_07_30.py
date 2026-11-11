"""PuzzleMadness Arrow Sudoku — 2025-07-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-07-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/7/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 5)], [(4, 4), (3, 4), (3, 3), (4, 2), (5, 1)])
    puzzle.add_arrow([(1, 8)], [(0, 7), (0, 6), (1, 7)])
    puzzle.add_arrow([(2, 7)], [(3, 6), (2, 5), (1, 5)])
    puzzle.add_arrow([(0, 4)], [(0, 3), (1, 3)])
    puzzle.add_arrow([(6, 6)], [(7, 7), (6, 8), (5, 8)])
    puzzle.add_arrow([(6, 2)], [(7, 2), (8, 1), (8, 0)])
    puzzle.add_arrow([(7, 3)], [(6, 3), (6, 4), (5, 3)])
    puzzle.add_arrow([(3, 1)], [(2, 2), (1, 1)])
    puzzle.add_arrow([(8, 5)], [(7, 5), (8, 4)])
    puzzle.add_arrow([(2, 1)], [(1, 0), (2, 0)])
    puzzle.add_arrow([(6, 1)], [(7, 1), (8, 2)])
    puzzle.add_arrow([(4, 8)], [(3, 7), (4, 7)])
    puzzle.add_arrow([(8, 6)], [(7, 6), (6, 5)])
    puzzle.add_arrow([(2, 4)], [(1, 4), (0, 5)])
    puzzle.add_arrow([(2, 6)], [(3, 5), (4, 6)])

    return puzzle
