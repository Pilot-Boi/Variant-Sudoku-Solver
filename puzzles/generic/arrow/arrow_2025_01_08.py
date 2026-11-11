"""PuzzleMadness Arrow Sudoku — 2025-01-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 2)], [(4, 3), (5, 2), (6, 2), (6, 1)])
    puzzle.add_arrow([(7, 8)], [(7, 7), (8, 8)])
    puzzle.add_arrow([(1, 4)], [(1, 3), (2, 2), (3, 1)])
    puzzle.add_arrow([(5, 5)], [(4, 5), (5, 6), (4, 7), (3, 7)])
    puzzle.add_arrow([(5, 3)], [(4, 4), (5, 4), (6, 3)])
    puzzle.add_arrow([(2, 7)], [(2, 6), (1, 6)])
    puzzle.add_arrow([(8, 5)], [(8, 6), (7, 5), (6, 5)])
    puzzle.add_arrow([(1, 0)], [(0, 0), (1, 1), (2, 0), (3, 0)])
    puzzle.add_arrow([(1, 2)], [(0, 3), (0, 2)])
    puzzle.add_arrow([(1, 7)], [(0, 8), (1, 8)])
    puzzle.add_arrow([(8, 2)], [(7, 2), (8, 1)])
    puzzle.add_arrow([(8, 3)], [(7, 4), (6, 4)])
    puzzle.add_arrow([(2, 3)], [(3, 3), (3, 2)])
    puzzle.add_arrow([(6, 6)], [(7, 6), (8, 7)])
    puzzle.add_arrow([(0, 6)], [(1, 5), (2, 5)])

    return puzzle
