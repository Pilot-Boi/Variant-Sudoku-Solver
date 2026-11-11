"""PuzzleMadness Arrow Sudoku — 2025-01-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 1, 0, 0, 0, 3, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 3)], [(3, 4), (2, 5)])
    puzzle.add_arrow([(4, 6)], [(5, 7), (6, 8)])
    puzzle.add_arrow([(1, 7)], [(2, 7), (2, 8), (3, 7)])
    puzzle.add_arrow([(0, 0)], [(1, 1), (1, 0)])
    puzzle.add_arrow([(4, 5)], [(5, 4), (4, 4), (4, 3)])
    puzzle.add_arrow([(3, 2)], [(2, 1), (3, 1), (4, 0)])
    puzzle.add_arrow([(6, 5)], [(7, 4), (8, 5)])
    puzzle.add_arrow([(8, 4)], [(7, 3), (8, 3), (8, 2)])
    puzzle.add_arrow([(5, 3)], [(5, 2), (6, 2)])
    puzzle.add_arrow([(6, 7)], [(7, 8), (7, 7)])
    puzzle.add_arrow([(0, 4)], [(0, 3), (1, 2), (0, 2)])
    puzzle.add_arrow([(6, 6)], [(5, 5), (5, 6)])
    puzzle.add_arrow([(5, 1)], [(6, 0), (5, 0), (6, 1)])
    puzzle.add_arrow([(1, 3)], [(1, 4), (0, 5)])
    puzzle.add_arrow([(2, 6)], [(1, 6), (1, 5)])

    return puzzle
