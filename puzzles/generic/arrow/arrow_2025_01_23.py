"""PuzzleMadness Arrow Sudoku — 2025-01-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 6, 0, 0, 0, 9, 1, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 3)], [(7, 3), (7, 2)])
    puzzle.add_arrow([(7, 0)], [(7, 1), (6, 0)])
    puzzle.add_arrow([(5, 1)], [(4, 1), (3, 1), (4, 2), (3, 3)])
    puzzle.add_arrow([(4, 7)], [(5, 6), (5, 7), (4, 6)])
    puzzle.add_arrow([(0, 6)], [(1, 7), (1, 6)])
    puzzle.add_arrow([(1, 5)], [(1, 4), (2, 5), (2, 4)])
    puzzle.add_arrow([(4, 4)], [(5, 4), (6, 5), (7, 5)])
    puzzle.add_arrow([(6, 7)], [(7, 7), (6, 8)])
    puzzle.add_arrow([(3, 7)], [(3, 8), (4, 8)])
    puzzle.add_arrow([(1, 1)], [(0, 2), (1, 2)])
    puzzle.add_arrow([(2, 1)], [(1, 0), (0, 1), (0, 0)])
    puzzle.add_arrow([(0, 3)], [(0, 4), (0, 5)])
    puzzle.add_arrow([(2, 2)], [(2, 3), (3, 2)])
    puzzle.add_arrow([(1, 8)], [(2, 7), (2, 6)])
    puzzle.add_arrow([(8, 8)], [(7, 8), (8, 7)])

    return puzzle
