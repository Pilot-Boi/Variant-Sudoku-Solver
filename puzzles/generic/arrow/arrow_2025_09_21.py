"""PuzzleMadness Arrow Sudoku — 2025-09-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 9],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 6)], [(4, 5), (3, 4), (4, 4)])
    puzzle.add_arrow([(7, 6)], [(7, 7), (7, 8)])
    puzzle.add_arrow([(2, 4)], [(3, 3), (4, 2), (5, 1)])
    puzzle.add_arrow([(7, 1)], [(6, 2), (5, 3)])
    puzzle.add_arrow([(1, 0)], [(2, 1), (1, 2), (0, 1)])
    puzzle.add_arrow([(0, 5)], [(0, 4), (1, 5), (1, 4)])
    puzzle.add_arrow([(4, 7)], [(3, 8), (3, 7), (2, 8), (2, 7)])
    puzzle.add_arrow([(8, 4)], [(7, 4), (7, 3), (6, 4)])
    puzzle.add_arrow([(5, 5)], [(5, 6), (4, 6)])
    puzzle.add_arrow([(7, 0)], [(6, 0), (5, 0), (4, 1)])
    puzzle.add_arrow([(0, 0)], [(1, 1), (0, 2)])
    puzzle.add_arrow([(2, 5)], [(2, 6), (1, 7)])
    puzzle.add_arrow([(6, 5)], [(7, 5), (8, 5)])
    puzzle.add_arrow([(8, 3)], [(8, 2), (7, 2)])
    puzzle.add_arrow([(6, 6)], [(6, 7), (5, 8)])
    puzzle.add_arrow([(2, 2)], [(1, 3), (2, 3)])

    return puzzle
