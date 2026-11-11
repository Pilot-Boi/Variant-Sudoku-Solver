"""PuzzleMadness Arrow Sudoku — 2025-09-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 5, 4, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 1)], [(6, 1), (5, 2), (6, 2)])
    puzzle.add_arrow([(1, 7)], [(2, 8), (3, 7)])
    puzzle.add_arrow([(7, 6)], [(6, 6), (5, 7), (4, 6), (5, 5)])
    puzzle.add_arrow([(2, 4)], [(1, 3), (0, 4), (0, 3)])
    puzzle.add_arrow([(3, 6)], [(4, 5), (3, 4), (2, 3)])
    puzzle.add_arrow([(3, 1)], [(4, 0), (4, 1), (3, 0)])
    puzzle.add_arrow([(1, 2)], [(1, 1), (2, 2), (2, 1)])
    puzzle.add_arrow([(0, 5)], [(0, 6), (0, 7), (1, 8)])
    puzzle.add_arrow([(8, 7)], [(7, 7), (6, 8)])
    puzzle.add_arrow([(6, 3)], [(7, 4), (6, 5)])
    puzzle.add_arrow([(8, 1)], [(7, 0), (6, 0)])
    puzzle.add_arrow([(7, 3)], [(8, 4), (8, 3)])
    puzzle.add_arrow([(4, 4)], [(5, 3), (4, 3)])
    puzzle.add_arrow([(4, 7)], [(3, 8), (4, 8)])
    puzzle.add_arrow([(1, 5)], [(1, 6), (2, 7)])

    return puzzle
