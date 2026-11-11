"""PuzzleMadness Arrow Sudoku — 2025-01-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 6)], [(5, 7), (5, 8), (4, 8)])
    puzzle.add_arrow([(3, 4)], [(4, 3), (5, 4), (4, 5)])
    puzzle.add_arrow([(7, 5)], [(7, 4), (8, 4)])
    puzzle.add_arrow([(5, 1)], [(6, 1), (7, 2), (7, 1)])
    puzzle.add_arrow([(2, 4)], [(2, 3), (2, 2)])
    puzzle.add_arrow([(3, 1)], [(3, 2), (2, 1)])
    puzzle.add_arrow([(8, 2)], [(8, 1), (7, 0)])
    puzzle.add_arrow([(3, 7)], [(2, 8), (2, 7)])
    puzzle.add_arrow([(6, 8)], [(6, 7), (7, 7)])
    puzzle.add_arrow([(4, 6)], [(3, 5), (2, 6)])
    puzzle.add_arrow([(1, 1)], [(0, 1), (1, 2)])
    puzzle.add_arrow([(0, 8)], [(0, 7), (1, 6)])
    puzzle.add_arrow([(0, 3)], [(0, 4), (0, 5)])
    puzzle.add_arrow([(6, 2)], [(5, 2), (6, 3)])
    puzzle.add_arrow([(4, 1)], [(5, 0), (4, 0)])
    puzzle.add_arrow([(6, 5)], [(6, 6), (5, 5), (6, 4)])
    puzzle.add_arrow([(2, 5)], [(1, 4), (1, 3)])
    puzzle.add_arrow([(1, 0)], [(2, 0), (3, 0)])

    return puzzle
