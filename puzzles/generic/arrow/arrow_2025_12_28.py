"""PuzzleMadness Arrow Sudoku — 2025-12-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-12-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/12/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 7, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(8, 4)], [(7, 4), (6, 5), (5, 4)])
    puzzle.add_arrow([(1, 8)], [(2, 7), (2, 6), (2, 5), (3, 6)])
    puzzle.add_arrow([(1, 3)], [(1, 2), (0, 3)])
    puzzle.add_arrow([(0, 1)], [(1, 1), (2, 0), (1, 0)])
    puzzle.add_arrow([(4, 1)], [(4, 0), (3, 1)])
    puzzle.add_arrow([(4, 2)], [(3, 2), (3, 3)])
    puzzle.add_arrow([(1, 5)], [(1, 4), (0, 4)])
    puzzle.add_arrow([(8, 8)], [(7, 8), (6, 8), (7, 7)])
    puzzle.add_arrow([(6, 0)], [(7, 0), (8, 1), (8, 0)])
    puzzle.add_arrow([(5, 5)], [(6, 4), (5, 3), (6, 3), (5, 2)])
    puzzle.add_arrow([(5, 6)], [(4, 6), (3, 5)])
    puzzle.add_arrow([(3, 4)], [(4, 3), (4, 4)])
    puzzle.add_arrow([(1, 7)], [(1, 6), (0, 5)])
    puzzle.add_arrow([(7, 3)], [(7, 2), (8, 2)])
    puzzle.add_arrow([(5, 7)], [(4, 7), (5, 8)])

    return puzzle
