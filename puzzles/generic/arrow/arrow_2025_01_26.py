"""PuzzleMadness Arrow Sudoku — 2025-01-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(0, 5)], [(1, 5), (0, 4), (0, 3)])
    puzzle.add_arrow([(6, 2)], [(7, 1), (6, 1)])
    puzzle.add_arrow([(8, 2)], [(7, 2), (6, 3), (5, 2), (5, 1), (5, 0)])
    puzzle.add_arrow([(4, 2)], [(3, 3), (4, 4)])
    puzzle.add_arrow([(1, 6)], [(2, 6), (3, 7)])
    puzzle.add_arrow([(6, 5)], [(5, 6), (4, 6), (3, 5)])
    puzzle.add_arrow([(0, 8)], [(1, 8), (1, 7), (2, 7)])
    puzzle.add_arrow([(3, 1)], [(2, 1), (1, 2), (0, 1)])
    puzzle.add_arrow([(2, 0)], [(3, 0), (4, 0)])
    puzzle.add_arrow([(6, 4)], [(7, 3), (7, 4), (8, 5)])
    puzzle.add_arrow([(5, 8)], [(6, 7), (6, 6)])
    puzzle.add_arrow([(2, 4)], [(1, 3), (1, 4)])
    puzzle.add_arrow([(7, 7)], [(8, 7), (7, 8)])
    puzzle.add_arrow([(7, 5)], [(7, 6), (8, 6)])
    puzzle.add_arrow([(5, 7)], [(4, 8), (4, 7)])
    puzzle.add_arrow([(8, 1)], [(8, 0), (7, 0)])

    return puzzle
