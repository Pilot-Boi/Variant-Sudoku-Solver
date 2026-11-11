"""PuzzleMadness Arrow Sudoku — 2025-10-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 0)], [(0, 0), (1, 1), (2, 2)])
    puzzle.add_arrow([(5, 0)], [(4, 0), (5, 1), (6, 0), (7, 0)])
    puzzle.add_arrow([(6, 8)], [(7, 8), (6, 7)])
    puzzle.add_arrow([(4, 4)], [(5, 5), (4, 6)])
    puzzle.add_arrow([(2, 5)], [(1, 4), (2, 4)])
    puzzle.add_arrow([(1, 5)], [(0, 5), (1, 6), (2, 7), (1, 7)])
    puzzle.add_arrow([(6, 3)], [(5, 3), (5, 2)])
    puzzle.add_arrow([(1, 3)], [(0, 3), (0, 4)])
    puzzle.add_arrow([(4, 1)], [(4, 2), (3, 3), (4, 3)])
    puzzle.add_arrow([(7, 3)], [(8, 4), (7, 5), (7, 4)])
    puzzle.add_arrow([(3, 6)], [(2, 6), (3, 5)])
    puzzle.add_arrow([(6, 1)], [(7, 1), (6, 2)])
    puzzle.add_arrow([(4, 7)], [(3, 8), (4, 8)])
    puzzle.add_arrow([(6, 5)], [(5, 6), (5, 7)])

    return puzzle
