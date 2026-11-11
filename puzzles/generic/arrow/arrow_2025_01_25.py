"""PuzzleMadness Arrow Sudoku — 2025-01-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(8, 7)], [(7, 7), (7, 8), (6, 8)])
    puzzle.add_arrow([(6, 5)], [(5, 5), (4, 5)])
    puzzle.add_arrow([(3, 5)], [(2, 6), (2, 5)])
    puzzle.add_arrow([(5, 7)], [(4, 7), (4, 6), (5, 6)])
    puzzle.add_arrow([(7, 1)], [(8, 2), (8, 1)])
    puzzle.add_arrow([(1, 0)], [(2, 0), (1, 1), (2, 1), (3, 0)])
    puzzle.add_arrow([(6, 3)], [(5, 2), (6, 2)])
    puzzle.add_arrow([(8, 3)], [(7, 3), (7, 4), (6, 4), (5, 3)])
    puzzle.add_arrow([(4, 1)], [(4, 2), (5, 1), (6, 1)])
    puzzle.add_arrow([(1, 6)], [(1, 7), (0, 8)])
    puzzle.add_arrow([(2, 4)], [(1, 5), (0, 4), (1, 4)])
    puzzle.add_arrow([(0, 0)], [(0, 1), (1, 2)])
    puzzle.add_arrow([(2, 7)], [(3, 8), (2, 8)])
    puzzle.add_arrow([(4, 3)], [(4, 4), (3, 3)])
    puzzle.add_arrow([(0, 2)], [(1, 3), (0, 3)])
    puzzle.add_arrow([(7, 6)], [(8, 5), (8, 4)])

    return puzzle
