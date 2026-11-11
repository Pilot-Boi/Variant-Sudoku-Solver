"""PuzzleMadness Arrow Sudoku — 2025-08-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-08-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/8/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 4, 3, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 2)], [(4, 1), (5, 0), (6, 0), (7, 1)])
    puzzle.add_arrow([(0, 6)], [(1, 5), (1, 6), (2, 7), (3, 8)])
    puzzle.add_arrow([(2, 0)], [(3, 1), (2, 1)])
    puzzle.add_arrow([(8, 4)], [(7, 4), (6, 3)])
    puzzle.add_arrow([(2, 5)], [(2, 4), (3, 4), (4, 4), (5, 5)])
    puzzle.add_arrow([(0, 4)], [(0, 3), (1, 3)])
    puzzle.add_arrow([(4, 3)], [(5, 3), (6, 2)])
    puzzle.add_arrow([(4, 5)], [(5, 6), (5, 7)])
    puzzle.add_arrow([(7, 7)], [(8, 7), (8, 8), (7, 8)])
    puzzle.add_arrow([(8, 3)], [(7, 3), (6, 4)])
    puzzle.add_arrow([(6, 6)], [(7, 6), (8, 6)])
    puzzle.add_arrow([(2, 3)], [(2, 2), (1, 2)])
    puzzle.add_arrow([(1, 7)], [(2, 6), (3, 7)])
    puzzle.add_arrow([(4, 7)], [(4, 6), (3, 5)])
    puzzle.add_arrow([(2, 8)], [(1, 8), (0, 7)])

    return puzzle
