"""PuzzleMadness Arrow Sudoku — 2025-11-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [9, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 1)], [(6, 2), (5, 3), (6, 3), (6, 4)])
    puzzle.add_arrow([(6, 5)], [(7, 5), (8, 4)])
    puzzle.add_arrow([(4, 1)], [(3, 0), (2, 1), (3, 2)])
    puzzle.add_arrow([(3, 7)], [(3, 6), (3, 5), (4, 5)])
    puzzle.add_arrow([(2, 6)], [(1, 7), (0, 8)])
    puzzle.add_arrow([(7, 7)], [(6, 8), (5, 8)])
    puzzle.add_arrow([(6, 1)], [(7, 1), (8, 1), (8, 0)])
    puzzle.add_arrow([(2, 2)], [(1, 2), (1, 1), (0, 2)])
    puzzle.add_arrow([(0, 5)], [(0, 6), (1, 5)])
    puzzle.add_arrow([(3, 8)], [(4, 7), (5, 7)])
    puzzle.add_arrow([(6, 6)], [(7, 6), (8, 5)])
    puzzle.add_arrow([(7, 0)], [(6, 0), (5, 0)])
    puzzle.add_arrow([(7, 2)], [(7, 3), (8, 2)])
    puzzle.add_arrow([(4, 4)], [(5, 4), (5, 5)])
    puzzle.add_arrow([(1, 8)], [(2, 7), (1, 6)])
    puzzle.add_arrow([(2, 5)], [(1, 4), (0, 3)])

    return puzzle
