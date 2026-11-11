"""PuzzleMadness Arrow Sudoku — 2025-11-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 4],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 1, 0, 0],
        [2, 0, 5, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 1)], [(5, 2), (4, 1), (3, 0)])
    puzzle.add_arrow([(0, 6)], [(1, 6), (0, 7), (1, 7)])
    puzzle.add_arrow([(7, 3)], [(7, 4), (8, 4), (7, 5)])
    puzzle.add_arrow([(4, 4)], [(5, 5), (6, 4)])
    puzzle.add_arrow([(8, 5)], [(7, 6), (6, 6), (7, 7)])
    puzzle.add_arrow([(4, 7)], [(3, 8), (2, 7), (3, 6)])
    puzzle.add_arrow([(1, 2)], [(1, 1), (0, 2)])
    puzzle.add_arrow([(0, 3)], [(1, 4), (0, 5), (0, 4)])
    puzzle.add_arrow([(2, 3)], [(3, 3), (2, 2), (1, 3)])
    puzzle.add_arrow([(3, 1)], [(2, 0), (2, 1)])
    puzzle.add_arrow([(8, 8)], [(7, 8), (8, 7)])
    puzzle.add_arrow([(7, 2)], [(6, 2), (5, 3), (4, 3)])
    puzzle.add_arrow([(7, 0)], [(7, 1), (8, 1)])
    puzzle.add_arrow([(2, 6)], [(2, 5), (2, 4)])
    puzzle.add_arrow([(4, 5)], [(3, 5), (4, 6)])
    puzzle.add_arrow([(6, 8)], [(5, 8), (6, 7)])
    puzzle.add_arrow([(4, 0)], [(5, 0), (6, 1)])

    return puzzle
