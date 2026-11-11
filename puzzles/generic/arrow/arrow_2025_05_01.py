"""PuzzleMadness Arrow Sudoku — 2025-05-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-05-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/5/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 3)], [(1, 2), (2, 2), (3, 2)])
    puzzle.add_arrow([(5, 0)], [(6, 1), (5, 2), (4, 1)])
    puzzle.add_arrow([(4, 7)], [(5, 6), (6, 5), (5, 4), (4, 4), (3, 3)])
    puzzle.add_arrow([(7, 8)], [(8, 8), (7, 7), (6, 8)])
    puzzle.add_arrow([(6, 6)], [(7, 5), (8, 6)])
    puzzle.add_arrow([(4, 6)], [(3, 7), (3, 8)])
    puzzle.add_arrow([(1, 6)], [(0, 5), (0, 6)])
    puzzle.add_arrow([(1, 8)], [(2, 7), (2, 8)])
    puzzle.add_arrow([(6, 2)], [(7, 1), (7, 0), (8, 1)])
    puzzle.add_arrow([(0, 4)], [(1, 5), (2, 5), (1, 4)])
    puzzle.add_arrow([(7, 2)], [(8, 3), (8, 2)])
    puzzle.add_arrow([(4, 5)], [(5, 5), (6, 4)])
    puzzle.add_arrow([(2, 6)], [(1, 7), (0, 7)])
    puzzle.add_arrow([(1, 0)], [(2, 1), (3, 0)])
    puzzle.add_arrow([(0, 1)], [(1, 1), (0, 2)])
    puzzle.add_arrow([(6, 7)], [(5, 7), (4, 8)])

    return puzzle
