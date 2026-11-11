"""PuzzleMadness Arrow Sudoku — 2025-09-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(8, 1)], [(8, 0), (7, 1)])
    puzzle.add_arrow([(8, 6)], [(8, 7), (7, 8), (6, 7), (5, 7)])
    puzzle.add_arrow([(4, 2)], [(3, 1), (4, 0)])
    puzzle.add_arrow([(5, 5)], [(4, 4), (4, 3), (5, 3), (6, 4)])
    puzzle.add_arrow([(1, 4)], [(0, 5), (1, 6), (1, 5)])
    puzzle.add_arrow([(3, 2)], [(2, 3), (2, 2)])
    puzzle.add_arrow([(7, 4)], [(6, 5), (7, 5)])
    puzzle.add_arrow([(5, 2)], [(6, 3), (6, 2)])
    puzzle.add_arrow([(1, 2)], [(2, 1), (3, 0)])
    puzzle.add_arrow([(3, 3)], [(2, 4), (2, 5)])
    puzzle.add_arrow([(1, 0)], [(0, 1), (0, 2)])
    puzzle.add_arrow([(5, 0)], [(6, 1), (7, 2)])
    puzzle.add_arrow([(4, 7)], [(5, 6), (4, 6)])
    puzzle.add_arrow([(4, 5)], [(3, 4), (3, 5)])
    puzzle.add_arrow([(6, 8)], [(5, 8), (4, 8)])
    puzzle.add_arrow([(6, 6)], [(7, 6), (7, 7)])
    puzzle.add_arrow([(2, 8)], [(1, 7), (0, 6)])

    return puzzle
