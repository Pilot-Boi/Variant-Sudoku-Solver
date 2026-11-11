"""PuzzleMadness Arrow Sudoku — 2025-06-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-06-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/6/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 9, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 5)], [(6, 5), (7, 6), (6, 7)])
    puzzle.add_arrow([(6, 4)], [(5, 3), (4, 4)])
    puzzle.add_arrow([(2, 7)], [(1, 8), (2, 8)])
    puzzle.add_arrow([(2, 0)], [(2, 1), (3, 2), (4, 3)])
    puzzle.add_arrow([(1, 4)], [(1, 5), (2, 4), (3, 5), (4, 6)])
    puzzle.add_arrow([(7, 1)], [(7, 2), (8, 1)])
    puzzle.add_arrow([(0, 1)], [(1, 2), (0, 3), (0, 4)])
    puzzle.add_arrow([(7, 4)], [(7, 3), (8, 2)])
    puzzle.add_arrow([(5, 0)], [(4, 1), (5, 2)])
    puzzle.add_arrow([(0, 7)], [(1, 7), (2, 6)])
    puzzle.add_arrow([(6, 6)], [(5, 7), (6, 8)])
    puzzle.add_arrow([(4, 7)], [(3, 6), (3, 7)])
    puzzle.add_arrow([(8, 8)], [(8, 7), (7, 8)])
    puzzle.add_arrow([(1, 3)], [(2, 2), (3, 1)])
    puzzle.add_arrow([(8, 0)], [(7, 0), (6, 0)])
    puzzle.add_arrow([(8, 3)], [(8, 4), (8, 5)])
    puzzle.add_arrow([(6, 1)], [(5, 1), (4, 0)])

    return puzzle
