"""PuzzleMadness Arrow Sudoku — 2025-05-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-05-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/5/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [2, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 3)], [(3, 2), (4, 3), (4, 2), (3, 1)])
    puzzle.add_arrow([(6, 8)], [(5, 7), (4, 8)])
    puzzle.add_arrow([(1, 5)], [(1, 4), (0, 3)])
    puzzle.add_arrow([(1, 1)], [(2, 1), (2, 0)])
    puzzle.add_arrow([(6, 7)], [(6, 6), (7, 7)])
    puzzle.add_arrow([(4, 6)], [(5, 5), (5, 4), (6, 5)])
    puzzle.add_arrow([(3, 8)], [(2, 7), (1, 6)])
    puzzle.add_arrow([(7, 1)], [(8, 2), (7, 2), (8, 3)])
    puzzle.add_arrow([(4, 4)], [(4, 5), (3, 6)])
    puzzle.add_arrow([(0, 6)], [(0, 7), (1, 7)])
    puzzle.add_arrow([(3, 4)], [(2, 4), (1, 3)])
    puzzle.add_arrow([(6, 1)], [(6, 2), (5, 3)])
    puzzle.add_arrow([(4, 0)], [(5, 1), (4, 1)])
    puzzle.add_arrow([(7, 4)], [(7, 5), (6, 4)])
    puzzle.add_arrow([(1, 0)], [(0, 1), (0, 2)])
    puzzle.add_arrow([(8, 6)], [(8, 5), (7, 6)])

    return puzzle
