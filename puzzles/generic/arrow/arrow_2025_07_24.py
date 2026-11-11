"""PuzzleMadness Arrow Sudoku — 2025-07-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-07-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/7/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 6, 3, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 6)], [(6, 7), (7, 7)])
    puzzle.add_arrow([(1, 3)], [(0, 4), (1, 4), (2, 3)])
    puzzle.add_arrow([(6, 2)], [(5, 2), (4, 1), (3, 0), (2, 1)])
    puzzle.add_arrow([(8, 0)], [(8, 1), (7, 1)])
    puzzle.add_arrow([(6, 4)], [(5, 4), (5, 5)])
    puzzle.add_arrow([(4, 7)], [(5, 6), (6, 6), (5, 7)])
    puzzle.add_arrow([(8, 4)], [(7, 3), (8, 3)])
    puzzle.add_arrow([(4, 3)], [(4, 4), (3, 4)])
    puzzle.add_arrow([(2, 6)], [(3, 5), (2, 4)])
    puzzle.add_arrow([(2, 0)], [(1, 1), (0, 2)])
    puzzle.add_arrow([(5, 8)], [(6, 8), (7, 8)])
    puzzle.add_arrow([(8, 6)], [(8, 5), (7, 5)])
    puzzle.add_arrow([(5, 0)], [(6, 1), (6, 0)])
    puzzle.add_arrow([(3, 1)], [(4, 2), (3, 2)])
    puzzle.add_arrow([(1, 6)], [(2, 7), (2, 8)])
    puzzle.add_arrow([(3, 7)], [(4, 8), (3, 8)])
    puzzle.add_arrow([(1, 8)], [(0, 8), (1, 7), (0, 6)])

    return puzzle
