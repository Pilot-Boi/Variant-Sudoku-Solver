"""PuzzleMadness Arrow Sudoku — 2025-01-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 3)], [(5, 3), (4, 2)])
    puzzle.add_arrow([(3, 4)], [(3, 5), (2, 6), (1, 6)])
    puzzle.add_arrow([(7, 5)], [(6, 5), (7, 4)])
    puzzle.add_arrow([(8, 1)], [(7, 1), (6, 0)])
    puzzle.add_arrow([(7, 6)], [(6, 7), (7, 8), (6, 8)])
    puzzle.add_arrow([(5, 8)], [(4, 7), (3, 7)])
    puzzle.add_arrow([(2, 7)], [(3, 8), (4, 8)])
    puzzle.add_arrow([(1, 5)], [(0, 6), (0, 7)])
    puzzle.add_arrow([(1, 1)], [(1, 2), (1, 3), (1, 4)])
    puzzle.add_arrow([(6, 1)], [(5, 1), (4, 1)])
    puzzle.add_arrow([(1, 0)], [(2, 1), (2, 2)])
    puzzle.add_arrow([(8, 5)], [(8, 4), (7, 3), (8, 3)])
    puzzle.add_arrow([(5, 5)], [(4, 5), (5, 4)])
    puzzle.add_arrow([(6, 3)], [(6, 2), (7, 2)])
    puzzle.add_arrow([(3, 2)], [(2, 3), (2, 4)])
    puzzle.add_arrow([(8, 6)], [(8, 7), (8, 8)])
    puzzle.add_arrow([(0, 3)], [(0, 2), (0, 1)])
    puzzle.add_arrow([(2, 8)], [(1, 7), (0, 8)])
    puzzle.add_arrow([(4, 0)], [(3, 1), (2, 0)])

    return puzzle
