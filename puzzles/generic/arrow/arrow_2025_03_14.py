"""PuzzleMadness Arrow Sudoku — 2025-03-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-03-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/3/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 6)], [(3, 6), (3, 7), (2, 7), (3, 8)])
    puzzle.add_arrow([(7, 2)], [(6, 1), (7, 0), (7, 1)])
    puzzle.add_arrow([(3, 0)], [(4, 1), (5, 1), (6, 2)])
    puzzle.add_arrow([(6, 5)], [(5, 5), (4, 5), (5, 4)])
    puzzle.add_arrow([(0, 5)], [(0, 6), (1, 5)])
    puzzle.add_arrow([(1, 1)], [(2, 2), (1, 2), (0, 2)])
    puzzle.add_arrow([(6, 0)], [(5, 0), (4, 0), (3, 1)])
    puzzle.add_arrow([(7, 4)], [(6, 3), (7, 3)])
    puzzle.add_arrow([(2, 5)], [(1, 4), (0, 3)])
    puzzle.add_arrow([(1, 7)], [(0, 7), (1, 6)])
    puzzle.add_arrow([(5, 6)], [(6, 7), (7, 6), (8, 5)])
    puzzle.add_arrow([(6, 6)], [(7, 7), (8, 6)])
    puzzle.add_arrow([(3, 2)], [(3, 3), (4, 4)])
    puzzle.add_arrow([(2, 1)], [(1, 0), (0, 0)])

    return puzzle
