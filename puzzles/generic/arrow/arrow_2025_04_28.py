"""PuzzleMadness Arrow Sudoku — 2025-04-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [2, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(8, 2)], [(7, 1), (6, 2), (6, 1)])
    puzzle.add_arrow([(2, 1)], [(3, 2), (4, 1), (5, 1)])
    puzzle.add_arrow([(1, 4)], [(0, 4), (1, 3)])
    puzzle.add_arrow([(4, 7)], [(4, 6), (5, 6), (6, 5), (5, 5)])
    puzzle.add_arrow([(4, 2)], [(5, 2), (4, 3)])
    puzzle.add_arrow([(8, 8)], [(7, 8), (6, 8), (5, 8)])
    puzzle.add_arrow([(2, 2)], [(3, 3), (2, 3), (1, 2)])
    puzzle.add_arrow([(6, 4)], [(7, 3), (7, 4)])
    puzzle.add_arrow([(0, 0)], [(1, 0), (2, 0), (1, 1)])
    puzzle.add_arrow([(1, 5)], [(0, 6), (0, 7), (0, 8)])
    puzzle.add_arrow([(3, 4)], [(4, 4), (3, 5)])
    puzzle.add_arrow([(7, 6)], [(8, 5), (8, 6)])
    puzzle.add_arrow([(2, 6)], [(1, 7), (2, 8)])
    puzzle.add_arrow([(4, 8)], [(3, 8), (2, 7)])
    puzzle.add_arrow([(3, 1)], [(4, 0), (5, 0)])
    puzzle.add_arrow([(5, 4)], [(4, 5), (3, 6)])
    puzzle.add_arrow([(8, 3)], [(8, 4), (7, 5)])

    return puzzle
