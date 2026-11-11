"""PuzzleMadness Arrow Sudoku — 2025-11-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 8, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 5)], [(3, 6), (2, 7)])
    puzzle.add_arrow([(4, 4)], [(4, 3), (5, 4)])
    puzzle.add_arrow([(3, 2)], [(3, 1), (2, 0), (1, 1)])
    puzzle.add_arrow([(6, 7)], [(7, 8), (6, 8), (5, 8)])
    puzzle.add_arrow([(7, 3)], [(7, 2), (6, 2)])
    puzzle.add_arrow([(5, 7)], [(4, 7), (3, 8)])
    puzzle.add_arrow([(1, 3)], [(2, 3), (1, 4)])
    puzzle.add_arrow([(0, 5)], [(0, 6), (1, 7)])
    puzzle.add_arrow([(8, 0)], [(7, 0), (8, 1)])
    puzzle.add_arrow([(5, 3)], [(4, 2), (5, 1), (4, 0)])
    puzzle.add_arrow([(7, 4)], [(7, 5), (6, 6), (5, 5)])
    puzzle.add_arrow([(8, 2)], [(8, 3), (8, 4)])
    puzzle.add_arrow([(2, 1)], [(1, 2), (0, 2)])
    puzzle.add_arrow([(8, 6)], [(8, 7), (7, 6)])
    puzzle.add_arrow([(0, 8)], [(0, 7), (1, 8)])
    puzzle.add_arrow([(1, 5)], [(2, 4), (3, 5)])
    puzzle.add_arrow([(6, 3)], [(6, 4), (6, 5)])

    return puzzle
