"""PuzzleMadness Arrow Sudoku — 2025-08-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-08-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/8/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 2, 0, 0, 0, 0, 0],
        [7, 0, 0, 3, 0, 2, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(0, 6)], [(1, 6), (1, 7), (1, 8)])
    puzzle.add_arrow([(2, 2)], [(2, 1), (2, 0), (3, 1)])
    puzzle.add_arrow([(3, 6)], [(4, 5), (5, 4), (6, 5)])
    puzzle.add_arrow([(5, 3)], [(4, 2), (3, 3), (2, 3)])
    puzzle.add_arrow([(4, 7)], [(5, 7), (4, 6)])
    puzzle.add_arrow([(0, 2)], [(0, 3), (0, 4)])
    puzzle.add_arrow([(6, 7)], [(7, 6), (8, 7), (8, 8)])
    puzzle.add_arrow([(7, 4)], [(6, 4), (6, 3)])
    puzzle.add_arrow([(1, 5)], [(2, 6), (3, 5)])
    puzzle.add_arrow([(8, 2)], [(8, 3), (8, 4)])
    puzzle.add_arrow([(6, 1)], [(6, 0), (5, 0)])
    puzzle.add_arrow([(7, 1)], [(7, 2), (8, 1), (7, 0)])
    puzzle.add_arrow([(1, 0)], [(1, 1), (0, 1)])
    puzzle.add_arrow([(2, 4)], [(1, 3), (1, 2)])
    puzzle.add_arrow([(6, 6)], [(7, 7), (7, 8)])

    return puzzle
