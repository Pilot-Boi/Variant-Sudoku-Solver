"""PuzzleMadness Arrow Sudoku — 2025-02-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 2, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 5)], [(4, 4), (5, 4), (5, 5), (5, 6)])
    puzzle.add_arrow([(3, 3)], [(3, 4), (2, 5)])
    puzzle.add_arrow([(5, 3)], [(4, 2), (5, 2)])
    puzzle.add_arrow([(4, 1)], [(3, 2), (2, 1), (1, 2), (1, 3)])
    puzzle.add_arrow([(3, 7)], [(3, 8), (4, 7)])
    puzzle.add_arrow([(1, 4)], [(0, 3), (0, 2)])
    puzzle.add_arrow([(6, 2)], [(7, 1), (8, 0), (7, 0)])
    puzzle.add_arrow([(8, 6)], [(8, 5), (7, 6), (8, 7)])
    puzzle.add_arrow([(5, 8)], [(6, 7), (6, 8)])
    puzzle.add_arrow([(7, 4)], [(7, 5), (8, 4)])
    puzzle.add_arrow([(7, 2)], [(6, 3), (6, 4)])
    puzzle.add_arrow([(1, 7)], [(0, 8), (0, 7)])
    puzzle.add_arrow([(2, 7)], [(2, 6), (1, 5)])
    puzzle.add_arrow([(7, 8)], [(7, 7), (8, 8)])
    puzzle.add_arrow([(0, 0)], [(0, 1), (1, 1)])
    puzzle.add_arrow([(4, 0)], [(3, 0), (3, 1)])
    puzzle.add_arrow([(5, 1)], [(5, 0), (6, 0)])

    return puzzle
