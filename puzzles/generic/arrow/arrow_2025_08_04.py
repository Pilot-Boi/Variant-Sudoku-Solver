"""PuzzleMadness Arrow Sudoku — 2025-08-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-08-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/8/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 2)], [(2, 3), (3, 3), (2, 4)])
    puzzle.add_arrow([(5, 8)], [(4, 7), (5, 6), (4, 5)])
    puzzle.add_arrow([(5, 3)], [(5, 2), (6, 2)])
    puzzle.add_arrow([(4, 0)], [(4, 1), (3, 2)])
    puzzle.add_arrow([(6, 1)], [(7, 1), (6, 0), (5, 0)])
    puzzle.add_arrow([(0, 0)], [(1, 1), (2, 1), (1, 0)])
    puzzle.add_arrow([(5, 5)], [(6, 6), (7, 5), (6, 5)])
    puzzle.add_arrow([(1, 7)], [(0, 8), (1, 8), (2, 7)])
    puzzle.add_arrow([(8, 3)], [(7, 3), (7, 4), (8, 5)])
    puzzle.add_arrow([(0, 1)], [(1, 2), (0, 2)])
    puzzle.add_arrow([(1, 5)], [(0, 5), (0, 4)])
    puzzle.add_arrow([(2, 5)], [(3, 4), (4, 4)])
    puzzle.add_arrow([(8, 1)], [(7, 0), (8, 0)])
    puzzle.add_arrow([(7, 8)], [(8, 7), (8, 6)])
    puzzle.add_arrow([(3, 6)], [(3, 7), (4, 8)])
    puzzle.add_arrow([(4, 2)], [(3, 1), (2, 0)])

    return puzzle
