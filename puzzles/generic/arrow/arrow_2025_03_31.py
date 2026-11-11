"""PuzzleMadness Arrow Sudoku — 2025-03-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-03-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/3/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 2)], [(4, 2), (4, 3), (5, 3), (6, 2)])
    puzzle.add_arrow([(7, 8)], [(6, 7), (5, 8)])
    puzzle.add_arrow([(6, 4)], [(7, 4), (6, 5)])
    puzzle.add_arrow([(1, 5)], [(1, 6), (2, 7), (3, 7)])
    puzzle.add_arrow([(2, 3)], [(3, 2), (2, 2)])
    puzzle.add_arrow([(0, 2)], [(1, 1), (1, 0), (0, 1)])
    puzzle.add_arrow([(4, 4)], [(3, 5), (4, 6), (5, 6)])
    puzzle.add_arrow([(8, 7)], [(7, 6), (8, 6)])
    puzzle.add_arrow([(5, 1)], [(6, 1), (6, 0)])
    puzzle.add_arrow([(8, 3)], [(8, 2), (8, 1)])
    puzzle.add_arrow([(1, 3)], [(0, 4), (1, 4)])
    puzzle.add_arrow([(2, 5)], [(3, 4), (3, 3)])
    puzzle.add_arrow([(1, 7)], [(1, 8), (2, 8)])
    puzzle.add_arrow([(3, 0)], [(3, 1), (4, 0)])
    puzzle.add_arrow([(6, 6)], [(7, 5), (8, 5)])

    return puzzle
