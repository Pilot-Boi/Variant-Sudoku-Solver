"""PuzzleMadness Arrow Sudoku — 2025-06-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-06-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/6/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 7],
        [0, 0, 0, 0, 0, 0, 8, 3, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 6)], [(2, 5), (1, 4), (2, 4)])
    puzzle.add_arrow([(5, 4)], [(4, 4), (4, 5), (5, 6)])
    puzzle.add_arrow([(6, 6)], [(5, 7), (6, 8), (7, 7)])
    puzzle.add_arrow([(7, 5)], [(7, 4), (8, 5), (7, 6)])
    puzzle.add_arrow([(1, 5)], [(2, 6), (1, 7), (0, 8)])
    puzzle.add_arrow([(3, 1)], [(3, 2), (3, 3), (4, 2)])
    puzzle.add_arrow([(7, 3)], [(6, 3), (6, 4)])
    puzzle.add_arrow([(7, 0)], [(7, 1), (8, 0)])
    puzzle.add_arrow([(2, 1)], [(2, 2), (1, 1), (0, 0)])
    puzzle.add_arrow([(4, 0)], [(4, 1), (5, 1)])
    puzzle.add_arrow([(1, 8)], [(2, 7), (3, 7)])
    puzzle.add_arrow([(6, 2)], [(7, 2), (6, 1), (5, 0)])
    puzzle.add_arrow([(0, 2)], [(0, 1), (1, 0)])
    puzzle.add_arrow([(8, 6)], [(8, 7), (8, 8)])
    puzzle.add_arrow([(0, 4)], [(0, 3), (1, 2)])
    puzzle.add_arrow([(0, 7)], [(0, 6), (0, 5)])

    return puzzle
