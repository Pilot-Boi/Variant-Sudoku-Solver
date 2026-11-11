"""PuzzleMadness Arrow Sudoku — 2025-01-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 4, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 3)], [(1, 2), (0, 3)])
    puzzle.add_arrow([(6, 3)], [(6, 4), (6, 5), (7, 4)])
    puzzle.add_arrow([(4, 6)], [(4, 5), (5, 4), (5, 3)])
    puzzle.add_arrow([(6, 1)], [(6, 2), (7, 1), (8, 2)])
    puzzle.add_arrow([(4, 0)], [(3, 0), (3, 1)])
    puzzle.add_arrow([(2, 2)], [(2, 1), (1, 1)])
    puzzle.add_arrow([(7, 5)], [(8, 4), (7, 3)])
    puzzle.add_arrow([(2, 5)], [(1, 5), (2, 6)])
    puzzle.add_arrow([(1, 6)], [(0, 5), (0, 4)])
    puzzle.add_arrow([(3, 8)], [(2, 7), (3, 6), (3, 7)])
    puzzle.add_arrow([(6, 7)], [(6, 8), (5, 7), (6, 6)])
    puzzle.add_arrow([(1, 8)], [(0, 7), (1, 7)])
    puzzle.add_arrow([(5, 2)], [(4, 2), (4, 1)])
    puzzle.add_arrow([(3, 3)], [(4, 3), (4, 4)])
    puzzle.add_arrow([(1, 4)], [(2, 3), (2, 4)])
    puzzle.add_arrow([(0, 0)], [(0, 1), (1, 0)])
    puzzle.add_arrow([(4, 8)], [(4, 7), (5, 6)])
    puzzle.add_arrow([(8, 5)], [(7, 6), (8, 6)])

    return puzzle
