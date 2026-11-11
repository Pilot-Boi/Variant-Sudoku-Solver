"""PuzzleMadness Arrow Sudoku — 2025-08-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-08-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/8/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 6, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 3)], [(8, 2), (7, 1), (6, 1)])
    puzzle.add_arrow([(5, 6)], [(5, 5), (6, 4), (5, 3), (6, 2)])
    puzzle.add_arrow([(2, 7)], [(3, 8), (2, 8), (1, 7)])
    puzzle.add_arrow([(1, 1)], [(2, 1), (2, 2)])
    puzzle.add_arrow([(6, 8)], [(7, 7), (6, 7)])
    puzzle.add_arrow([(5, 4)], [(4, 5), (4, 6)])
    puzzle.add_arrow([(4, 0)], [(3, 1), (4, 1), (3, 0)])
    puzzle.add_arrow([(3, 7)], [(4, 7), (5, 8)])
    puzzle.add_arrow([(1, 5)], [(2, 4), (3, 4), (4, 3)])
    puzzle.add_arrow([(7, 5)], [(6, 5), (7, 6), (8, 5)])
    puzzle.add_arrow([(0, 1)], [(0, 2), (0, 3)])
    puzzle.add_arrow([(0, 4)], [(0, 5), (1, 6)])
    puzzle.add_arrow([(8, 1)], [(7, 2), (6, 3)])
    puzzle.add_arrow([(0, 8)], [(1, 8), (0, 7)])

    return puzzle
