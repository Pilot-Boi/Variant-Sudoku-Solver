"""PuzzleMadness Arrow Sudoku — 2025-01-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 4],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 3)], [(3, 3), (3, 4)])
    puzzle.add_arrow([(0, 6)], [(1, 5), (2, 5), (2, 6), (1, 6)])
    puzzle.add_arrow([(6, 3)], [(7, 2), (8, 3)])
    puzzle.add_arrow([(6, 2)], [(5, 1), (6, 0)])
    puzzle.add_arrow([(6, 4)], [(7, 5), (8, 4)])
    puzzle.add_arrow([(7, 6)], [(6, 7), (6, 8)])
    puzzle.add_arrow([(2, 0)], [(3, 1), (2, 2)])
    puzzle.add_arrow([(2, 8)], [(3, 7), (4, 8)])
    puzzle.add_arrow([(5, 5)], [(6, 5), (7, 4)])
    puzzle.add_arrow([(0, 0)], [(0, 1), (1, 0)])
    puzzle.add_arrow([(7, 7)], [(8, 8), (8, 7), (8, 6)])
    puzzle.add_arrow([(1, 3)], [(0, 4), (0, 3), (0, 2)])
    puzzle.add_arrow([(3, 2)], [(2, 1), (1, 1)])
    puzzle.add_arrow([(5, 8)], [(5, 7), (4, 6), (3, 6)])
    puzzle.add_arrow([(6, 1)], [(5, 0), (4, 0), (3, 0)])
    puzzle.add_arrow([(0, 8)], [(1, 8), (1, 7)])
    puzzle.add_arrow([(3, 5)], [(4, 5), (5, 6)])
    puzzle.add_arrow([(4, 4)], [(5, 4), (4, 3)])

    return puzzle
