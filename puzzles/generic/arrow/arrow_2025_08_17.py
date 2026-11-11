"""PuzzleMadness Arrow Sudoku — 2025-08-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-08-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/8/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 8)], [(3, 8), (4, 7), (3, 6), (4, 5)])
    puzzle.add_arrow([(5, 4)], [(5, 3), (6, 3), (7, 4), (7, 5), (8, 6)])
    puzzle.add_arrow([(6, 2)], [(5, 1), (6, 1)])
    puzzle.add_arrow([(4, 1)], [(4, 0), (3, 1)])
    puzzle.add_arrow([(0, 2)], [(1, 2), (0, 1)])
    puzzle.add_arrow([(1, 4)], [(1, 5), (2, 4), (1, 3)])
    puzzle.add_arrow([(2, 2)], [(2, 3), (3, 4)])
    puzzle.add_arrow([(6, 7)], [(7, 7), (6, 8)])
    puzzle.add_arrow([(0, 0)], [(1, 1), (1, 0), (2, 0)])
    puzzle.add_arrow([(3, 7)], [(2, 7), (2, 8)])
    puzzle.add_arrow([(7, 6)], [(6, 6), (5, 5)])
    puzzle.add_arrow([(3, 2)], [(4, 2), (5, 2)])
    puzzle.add_arrow([(7, 1)], [(7, 0), (8, 1)])
    puzzle.add_arrow([(1, 6)], [(0, 5), (0, 4)])
    puzzle.add_arrow([(0, 7)], [(0, 8), (1, 7)])

    return puzzle
