"""PuzzleMadness Arrow Sudoku — 2025-12-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-12-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/12/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 8)], [(1, 7), (1, 6)])
    puzzle.add_arrow([(2, 4)], [(2, 3), (3, 3)])
    puzzle.add_arrow([(4, 8)], [(3, 8), (2, 7)])
    puzzle.add_arrow([(0, 6)], [(1, 5), (2, 6), (3, 6)])
    puzzle.add_arrow([(5, 4)], [(4, 3), (4, 4), (5, 3)])
    puzzle.add_arrow([(6, 8)], [(6, 7), (5, 6)])
    puzzle.add_arrow([(7, 5)], [(7, 4), (6, 5)])
    puzzle.add_arrow([(3, 0)], [(2, 0), (1, 0)])
    puzzle.add_arrow([(3, 7)], [(4, 6), (4, 7)])
    puzzle.add_arrow([(3, 1)], [(4, 2), (3, 2)])
    puzzle.add_arrow([(1, 2)], [(2, 1), (2, 2)])
    puzzle.add_arrow([(6, 3)], [(6, 2), (7, 3)])
    puzzle.add_arrow([(0, 5)], [(1, 4), (0, 4)])
    puzzle.add_arrow([(8, 3)], [(8, 2), (7, 1)])
    puzzle.add_arrow([(1, 3)], [(0, 2), (0, 1)])
    puzzle.add_arrow([(7, 0)], [(6, 1), (5, 0), (4, 0)])
    puzzle.add_arrow([(6, 6)], [(7, 7), (7, 8)])

    return puzzle
