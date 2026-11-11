"""PuzzleMadness Arrow Sudoku — 2025-06-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-06-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/6/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 3, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 6)], [(4, 5), (4, 4), (5, 5)])
    puzzle.add_arrow([(8, 1)], [(7, 2), (7, 1)])
    puzzle.add_arrow([(5, 2)], [(6, 2), (6, 1), (5, 1)])
    puzzle.add_arrow([(1, 8)], [(2, 8), (3, 7), (2, 6)])
    puzzle.add_arrow([(3, 1)], [(3, 0), (2, 0), (1, 1), (2, 2)])
    puzzle.add_arrow([(0, 2)], [(1, 3), (0, 3), (1, 4)])
    puzzle.add_arrow([(5, 4)], [(6, 4), (6, 5), (7, 6)])
    puzzle.add_arrow([(2, 5)], [(1, 6), (0, 7)])
    puzzle.add_arrow([(1, 5)], [(0, 4), (0, 5)])
    puzzle.add_arrow([(6, 8)], [(5, 8), (6, 7)])
    puzzle.add_arrow([(4, 1)], [(4, 2), (4, 3)])
    puzzle.add_arrow([(7, 4)], [(8, 4), (8, 5), (8, 6)])
    puzzle.add_arrow([(3, 5)], [(3, 6), (4, 7)])
    puzzle.add_arrow([(7, 7)], [(8, 8), (8, 7)])
    puzzle.add_arrow([(2, 7)], [(1, 7), (0, 8)])

    return puzzle
