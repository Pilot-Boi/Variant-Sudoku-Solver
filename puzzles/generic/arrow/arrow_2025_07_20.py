"""PuzzleMadness Arrow Sudoku — 2025-07-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-07-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/7/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 9, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 7, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 2)], [(5, 2), (4, 1)])
    puzzle.add_arrow([(4, 6)], [(3, 7), (2, 6), (1, 7)])
    puzzle.add_arrow([(5, 8)], [(4, 7), (3, 8)])
    puzzle.add_arrow([(4, 5)], [(4, 4), (3, 4), (2, 4), (1, 5)])
    puzzle.add_arrow([(8, 4)], [(7, 5), (6, 5), (6, 6)])
    puzzle.add_arrow([(5, 3)], [(4, 3), (3, 3)])
    puzzle.add_arrow([(5, 1)], [(5, 0), (6, 0), (7, 0)])
    puzzle.add_arrow([(7, 2)], [(6, 3), (6, 2)])
    puzzle.add_arrow([(3, 2)], [(2, 2), (1, 1), (2, 1)])
    puzzle.add_arrow([(1, 3)], [(0, 4), (0, 3)])
    puzzle.add_arrow([(8, 7)], [(8, 6), (8, 5)])
    puzzle.add_arrow([(0, 6)], [(1, 6), (0, 7)])
    puzzle.add_arrow([(7, 7)], [(8, 8), (7, 8)])
    puzzle.add_arrow([(7, 1)], [(8, 2), (8, 1)])
    puzzle.add_arrow([(0, 2)], [(0, 1), (1, 0)])
    puzzle.add_arrow([(5, 5)], [(5, 6), (5, 7)])

    return puzzle
