"""PuzzleMadness Arrow Sudoku — 2025-10-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 8)], [(2, 7), (1, 6), (1, 7)])
    puzzle.add_arrow([(7, 2)], [(6, 1), (5, 1)])
    puzzle.add_arrow([(1, 2)], [(0, 3), (1, 4), (1, 3)])
    puzzle.add_arrow([(4, 5)], [(5, 5), (5, 4)])
    puzzle.add_arrow([(6, 7)], [(5, 7), (6, 6)])
    puzzle.add_arrow([(4, 2)], [(3, 2), (2, 3)])
    puzzle.add_arrow([(3, 5)], [(3, 6), (3, 7)])
    puzzle.add_arrow([(1, 1)], [(0, 2), (0, 1), (1, 0)])
    puzzle.add_arrow([(8, 3)], [(8, 2), (7, 3), (6, 2)])
    puzzle.add_arrow([(8, 6)], [(8, 7), (7, 8), (6, 8)])
    puzzle.add_arrow([(7, 6)], [(7, 5), (8, 5), (7, 4)])
    puzzle.add_arrow([(3, 1)], [(2, 2), (2, 1)])
    puzzle.add_arrow([(8, 0)], [(8, 1), (7, 0)])
    puzzle.add_arrow([(4, 8)], [(3, 8), (4, 7)])
    puzzle.add_arrow([(5, 2)], [(4, 3), (4, 4)])
    puzzle.add_arrow([(2, 4)], [(3, 4), (3, 3)])
    puzzle.add_arrow([(6, 0)], [(5, 0), (4, 0), (3, 0)])

    return puzzle
