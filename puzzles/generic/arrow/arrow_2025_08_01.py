"""PuzzleMadness Arrow Sudoku — 2025-08-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-08-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/8/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 7)], [(3, 6), (2, 7), (1, 8), (0, 8)])
    puzzle.add_arrow([(1, 6)], [(1, 5), (0, 4), (0, 3)])
    puzzle.add_arrow([(3, 4)], [(4, 5), (4, 6)])
    puzzle.add_arrow([(6, 8)], [(7, 7), (6, 7)])
    puzzle.add_arrow([(6, 1)], [(5, 0), (5, 1), (4, 1)])
    puzzle.add_arrow([(5, 4)], [(4, 3), (4, 2)])
    puzzle.add_arrow([(7, 3)], [(8, 2), (7, 1)])
    puzzle.add_arrow([(0, 2)], [(1, 2), (2, 3)])
    puzzle.add_arrow([(6, 6)], [(6, 5), (7, 4)])
    puzzle.add_arrow([(2, 5)], [(2, 4), (3, 3), (3, 2)])
    puzzle.add_arrow([(7, 6)], [(7, 5), (8, 4)])
    puzzle.add_arrow([(0, 1)], [(1, 1), (2, 0)])
    puzzle.add_arrow([(8, 1)], [(7, 2), (6, 2), (6, 3)])
    puzzle.add_arrow([(1, 7)], [(0, 7), (0, 6)])
    puzzle.add_arrow([(3, 0)], [(2, 1), (2, 2)])

    return puzzle
