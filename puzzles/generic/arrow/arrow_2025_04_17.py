"""PuzzleMadness Arrow Sudoku — 2025-04-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 8)], [(1, 7), (2, 6), (1, 5)])
    puzzle.add_arrow([(6, 1)], [(7, 1), (7, 2), (6, 3), (5, 3)])
    puzzle.add_arrow([(6, 5)], [(5, 4), (4, 3)])
    puzzle.add_arrow([(5, 7)], [(6, 8), (7, 8)])
    puzzle.add_arrow([(3, 1)], [(2, 2), (1, 2), (2, 3)])
    puzzle.add_arrow([(5, 1)], [(4, 2), (4, 1)])
    puzzle.add_arrow([(4, 8)], [(3, 7), (3, 8), (2, 7)])
    puzzle.add_arrow([(1, 4)], [(2, 5), (3, 6), (3, 5)])
    puzzle.add_arrow([(1, 6)], [(0, 7), (0, 8)])
    puzzle.add_arrow([(2, 1)], [(1, 1), (0, 1)])
    puzzle.add_arrow([(7, 6)], [(8, 6), (8, 7)])
    puzzle.add_arrow([(4, 6)], [(5, 5), (5, 6)])
    puzzle.add_arrow([(7, 3)], [(7, 4), (6, 4)])
    puzzle.add_arrow([(2, 0)], [(3, 0), (4, 0), (5, 0)])
    puzzle.add_arrow([(6, 0)], [(7, 0), (8, 0)])

    return puzzle
