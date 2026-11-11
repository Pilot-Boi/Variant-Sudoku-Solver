"""PuzzleMadness Arrow Sudoku — 2025-08-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-08-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/8/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 6)], [(4, 5), (3, 6), (3, 7), (4, 8)])
    puzzle.add_arrow([(7, 6)], [(6, 7), (7, 8), (7, 7)])
    puzzle.add_arrow([(7, 4)], [(8, 5), (8, 6)])
    puzzle.add_arrow([(3, 2)], [(3, 3), (2, 2)])
    puzzle.add_arrow([(4, 1)], [(4, 0), (5, 1), (5, 2)])
    puzzle.add_arrow([(2, 8)], [(1, 7), (0, 8)])
    puzzle.add_arrow([(6, 1)], [(7, 2), (7, 1)])
    puzzle.add_arrow([(0, 5)], [(0, 4), (1, 4), (1, 5)])
    puzzle.add_arrow([(2, 3)], [(1, 3), (0, 3)])
    puzzle.add_arrow([(0, 6)], [(1, 6), (2, 5), (3, 4)])
    puzzle.add_arrow([(5, 5)], [(5, 4), (6, 5)])
    puzzle.add_arrow([(1, 8)], [(2, 7), (2, 6)])
    puzzle.add_arrow([(3, 1)], [(2, 1), (1, 1), (0, 2)])
    puzzle.add_arrow([(4, 4)], [(5, 3), (4, 3)])
    puzzle.add_arrow([(5, 8)], [(5, 7), (4, 6)])
    puzzle.add_arrow([(8, 1)], [(8, 0), (7, 0), (6, 0)])

    return puzzle
