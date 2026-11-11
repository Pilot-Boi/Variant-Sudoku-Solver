"""PuzzleMadness Arrow Sudoku — 2025-04-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 7, 0, 8],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 7)], [(6, 6), (6, 5), (7, 4), (6, 4)])
    puzzle.add_arrow([(8, 3)], [(8, 2), (7, 2), (7, 3)])
    puzzle.add_arrow([(0, 3)], [(1, 4), (2, 5)])
    puzzle.add_arrow([(1, 7)], [(2, 8), (3, 7), (4, 7), (5, 6)])
    puzzle.add_arrow([(6, 3)], [(6, 2), (5, 3)])
    puzzle.add_arrow([(3, 6)], [(2, 6), (2, 7)])
    puzzle.add_arrow([(4, 2)], [(4, 3), (3, 2), (3, 1)])
    puzzle.add_arrow([(1, 1)], [(0, 2), (0, 1)])
    puzzle.add_arrow([(5, 2)], [(6, 1), (5, 0)])
    puzzle.add_arrow([(8, 5)], [(8, 6), (8, 7)])
    puzzle.add_arrow([(3, 4)], [(4, 4), (4, 5)])
    puzzle.add_arrow([(4, 1)], [(4, 0), (5, 1)])
    puzzle.add_arrow([(1, 3)], [(2, 3), (3, 3)])
    puzzle.add_arrow([(0, 5)], [(1, 5), (0, 6)])
    puzzle.add_arrow([(7, 1)], [(7, 0), (6, 0)])
    puzzle.add_arrow([(7, 8)], [(6, 8), (5, 7)])
    puzzle.add_arrow([(0, 0)], [(1, 0), (2, 1)])

    return puzzle
