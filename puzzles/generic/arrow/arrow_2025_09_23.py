"""PuzzleMadness Arrow Sudoku — 2025-09-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 3)], [(5, 4), (4, 5)])
    puzzle.add_arrow([(2, 4)], [(3, 5), (3, 6)])
    puzzle.add_arrow([(5, 3)], [(6, 3), (7, 2), (7, 3)])
    puzzle.add_arrow([(7, 7)], [(7, 6), (6, 6), (6, 7)])
    puzzle.add_arrow([(1, 8)], [(2, 8), (2, 7), (3, 8)])
    puzzle.add_arrow([(3, 4)], [(2, 3), (3, 2), (4, 1)])
    puzzle.add_arrow([(2, 1)], [(1, 1), (1, 0), (2, 0)])
    puzzle.add_arrow([(6, 5)], [(5, 5), (4, 4)])
    puzzle.add_arrow([(1, 5)], [(0, 4), (1, 3)])
    puzzle.add_arrow([(7, 8)], [(8, 8), (8, 7)])
    puzzle.add_arrow([(6, 2)], [(7, 1), (8, 2)])
    puzzle.add_arrow([(6, 1)], [(7, 0), (8, 0)])
    puzzle.add_arrow([(5, 8)], [(5, 7), (4, 6)])
    puzzle.add_arrow([(4, 2)], [(5, 1), (5, 0)])
    puzzle.add_arrow([(1, 6)], [(0, 7), (0, 8)])
    puzzle.add_arrow([(7, 4)], [(6, 4), (7, 5)])
    puzzle.add_arrow([(1, 2)], [(0, 1), (0, 0)])

    return puzzle
