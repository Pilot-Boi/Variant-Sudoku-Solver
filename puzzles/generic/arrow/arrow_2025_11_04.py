"""PuzzleMadness Arrow Sudoku — 2025-11-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 6)], [(0, 7), (1, 7)])
    puzzle.add_arrow([(4, 4)], [(5, 4), (5, 5), (6, 6), (7, 6), (8, 5)])
    puzzle.add_arrow([(8, 1)], [(7, 0), (6, 1)])
    puzzle.add_arrow([(4, 3)], [(3, 2), (2, 1), (3, 0)])
    puzzle.add_arrow([(1, 2)], [(2, 3), (3, 3)])
    puzzle.add_arrow([(3, 6)], [(4, 6), (4, 7), (5, 8)])
    puzzle.add_arrow([(7, 4)], [(8, 4), (8, 3), (8, 2)])
    puzzle.add_arrow([(5, 7)], [(4, 8), (3, 8)])
    puzzle.add_arrow([(2, 8)], [(2, 7), (1, 8)])
    puzzle.add_arrow([(6, 7)], [(7, 7), (8, 6)])
    puzzle.add_arrow([(4, 1)], [(4, 0), (3, 1)])
    puzzle.add_arrow([(1, 5)], [(1, 4), (0, 4), (0, 3)])
    puzzle.add_arrow([(2, 0)], [(1, 1), (0, 0)])
    puzzle.add_arrow([(6, 3)], [(6, 2), (7, 1)])
    puzzle.add_arrow([(2, 6)], [(3, 5), (2, 4)])
    puzzle.add_arrow([(0, 2)], [(0, 1), (1, 0)])
    puzzle.add_arrow([(7, 3)], [(6, 4), (7, 5)])

    return puzzle
