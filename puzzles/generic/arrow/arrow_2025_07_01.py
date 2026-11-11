"""PuzzleMadness Arrow Sudoku — 2025-07-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-07-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/7/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 3)], [(3, 2), (2, 3), (1, 4)])
    puzzle.add_arrow([(4, 4)], [(4, 3), (4, 2), (4, 1)])
    puzzle.add_arrow([(8, 5)], [(8, 6), (7, 5), (7, 4), (7, 3)])
    puzzle.add_arrow([(3, 6)], [(4, 5), (4, 6), (5, 7)])
    puzzle.add_arrow([(7, 1)], [(7, 0), (8, 0)])
    puzzle.add_arrow([(5, 3)], [(5, 4), (5, 5)])
    puzzle.add_arrow([(2, 8)], [(1, 7), (0, 8), (0, 7)])
    puzzle.add_arrow([(1, 3)], [(1, 2), (2, 1), (2, 0)])
    puzzle.add_arrow([(4, 7)], [(3, 8), (4, 8)])
    puzzle.add_arrow([(5, 2)], [(6, 1), (7, 2)])
    puzzle.add_arrow([(0, 4)], [(1, 5), (0, 6)])
    puzzle.add_arrow([(6, 7)], [(7, 7), (8, 8)])
    puzzle.add_arrow([(2, 6)], [(3, 7), (2, 7)])
    puzzle.add_arrow([(1, 6)], [(2, 5), (3, 4)])
    puzzle.add_arrow([(5, 0)], [(5, 1), (6, 2)])
    puzzle.add_arrow([(1, 0)], [(0, 1), (1, 1)])

    return puzzle
