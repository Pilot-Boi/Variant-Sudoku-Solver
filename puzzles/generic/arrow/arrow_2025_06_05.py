"""PuzzleMadness Arrow Sudoku — 2025-06-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-06-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/6/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [9, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 5)], [(4, 6), (5, 6), (6, 7)])
    puzzle.add_arrow([(7, 1)], [(6, 2), (5, 1)])
    puzzle.add_arrow([(8, 6)], [(7, 5), (7, 6)])
    puzzle.add_arrow([(1, 8)], [(2, 8), (1, 7)])
    puzzle.add_arrow([(0, 4)], [(1, 4), (0, 3), (1, 2), (2, 2)])
    puzzle.add_arrow([(7, 3)], [(7, 4), (6, 5)])
    puzzle.add_arrow([(3, 4)], [(3, 5), (3, 6), (2, 7)])
    puzzle.add_arrow([(0, 6)], [(0, 5), (1, 5), (2, 6)])
    puzzle.add_arrow([(3, 2)], [(4, 2), (4, 3), (5, 3)])
    puzzle.add_arrow([(1, 6)], [(0, 7), (0, 8)])
    puzzle.add_arrow([(5, 2)], [(4, 1), (3, 0)])
    puzzle.add_arrow([(6, 3)], [(5, 4), (6, 4)])
    puzzle.add_arrow([(7, 8)], [(7, 7), (8, 8)])
    puzzle.add_arrow([(5, 7)], [(5, 8), (6, 8)])
    puzzle.add_arrow([(6, 1)], [(5, 0), (4, 0)])
    puzzle.add_arrow([(0, 0)], [(0, 1), (1, 1)])
    puzzle.add_arrow([(4, 7)], [(3, 7), (3, 8)])

    return puzzle
