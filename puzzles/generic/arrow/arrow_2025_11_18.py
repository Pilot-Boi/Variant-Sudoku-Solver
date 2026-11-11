"""PuzzleMadness Arrow Sudoku — 2025-11-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(8, 3)], [(7, 2), (6, 3), (6, 4)])
    puzzle.add_arrow([(5, 7)], [(4, 8), (3, 7), (2, 6), (3, 5)])
    puzzle.add_arrow([(0, 1)], [(0, 2), (1, 3)])
    puzzle.add_arrow([(4, 5)], [(5, 5), (6, 5), (6, 6)])
    puzzle.add_arrow([(5, 1)], [(4, 1), (3, 1), (4, 2), (5, 3)])
    puzzle.add_arrow([(0, 7)], [(1, 6), (1, 7), (0, 6)])
    puzzle.add_arrow([(5, 0)], [(6, 1), (7, 0), (8, 0)])
    puzzle.add_arrow([(4, 6)], [(5, 6), (4, 7)])
    puzzle.add_arrow([(1, 2)], [(0, 3), (0, 4), (0, 5)])
    puzzle.add_arrow([(7, 6)], [(7, 7), (8, 7)])
    puzzle.add_arrow([(3, 0)], [(2, 0), (1, 1), (2, 1)])
    puzzle.add_arrow([(8, 6)], [(8, 5), (8, 4)])
    puzzle.add_arrow([(4, 3)], [(3, 2), (2, 3)])
    puzzle.add_arrow([(6, 8)], [(5, 8), (6, 7)])

    return puzzle
