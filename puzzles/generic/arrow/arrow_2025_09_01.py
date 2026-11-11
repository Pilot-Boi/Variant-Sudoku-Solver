"""PuzzleMadness Arrow Sudoku — 2025-09-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 4)], [(2, 5), (3, 4), (4, 4)])
    puzzle.add_arrow([(0, 8)], [(1, 7), (1, 6), (0, 6)])
    puzzle.add_arrow([(1, 1)], [(1, 2), (2, 1), (1, 0)])
    puzzle.add_arrow([(3, 1)], [(3, 0), (4, 0), (5, 0)])
    puzzle.add_arrow([(6, 0)], [(7, 1), (8, 2), (7, 3)])
    puzzle.add_arrow([(7, 4)], [(6, 4), (5, 4), (6, 3)])
    puzzle.add_arrow([(2, 7)], [(3, 8), (4, 7)])
    puzzle.add_arrow([(8, 6)], [(7, 7), (8, 8)])
    puzzle.add_arrow([(6, 6)], [(5, 7), (4, 6)])
    puzzle.add_arrow([(6, 2)], [(6, 1), (7, 0)])
    puzzle.add_arrow([(5, 5)], [(5, 6), (6, 7)])
    puzzle.add_arrow([(3, 3)], [(2, 3), (2, 2)])
    puzzle.add_arrow([(5, 8)], [(4, 8), (3, 7)])
    puzzle.add_arrow([(4, 2)], [(5, 1), (5, 2)])
    puzzle.add_arrow([(7, 2)], [(8, 1), (8, 0)])
    puzzle.add_arrow([(0, 5)], [(1, 5), (0, 4), (0, 3)])
    puzzle.add_arrow([(2, 6)], [(3, 5), (3, 6)])

    return puzzle
