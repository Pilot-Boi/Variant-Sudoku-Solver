"""PuzzleMadness Arrow Sudoku — 2025-07-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-07-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/7/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 1, 0, 7, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 6)], [(2, 6), (2, 7), (3, 6)])
    puzzle.add_arrow([(1, 2)], [(2, 3), (1, 3), (2, 4)])
    puzzle.add_arrow([(7, 3)], [(7, 2), (7, 1), (7, 0)])
    puzzle.add_arrow([(4, 1)], [(4, 2), (5, 3), (6, 2)])
    puzzle.add_arrow([(5, 8)], [(6, 8), (5, 7)])
    puzzle.add_arrow([(5, 6)], [(6, 5), (7, 6)])
    puzzle.add_arrow([(0, 4)], [(1, 4), (0, 3), (0, 2)])
    puzzle.add_arrow([(2, 1)], [(1, 0), (2, 0)])
    puzzle.add_arrow([(6, 1)], [(5, 1), (4, 0)])
    puzzle.add_arrow([(1, 7)], [(0, 7), (1, 8)])
    puzzle.add_arrow([(6, 6)], [(7, 5), (8, 5)])
    puzzle.add_arrow([(4, 4)], [(3, 4), (4, 5), (5, 5)])
    puzzle.add_arrow([(0, 5)], [(1, 5), (0, 6)])
    puzzle.add_arrow([(7, 4)], [(8, 4), (8, 3)])
    puzzle.add_arrow([(7, 7)], [(8, 8), (7, 8)])
    puzzle.add_arrow([(6, 3)], [(5, 4), (6, 4)])
    puzzle.add_arrow([(8, 0)], [(8, 1), (8, 2)])
    puzzle.add_arrow([(2, 2)], [(3, 1), (3, 0)])
    puzzle.add_arrow([(3, 5)], [(4, 6), (4, 7)])

    return puzzle
