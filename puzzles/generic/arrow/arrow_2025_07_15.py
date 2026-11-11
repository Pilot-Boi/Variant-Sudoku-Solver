"""PuzzleMadness Arrow Sudoku — 2025-07-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-07-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/7/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [9, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 2, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(0, 6)], [(1, 6), (2, 7), (3, 6)])
    puzzle.add_arrow([(6, 3)], [(7, 4), (8, 3)])
    puzzle.add_arrow([(7, 6)], [(6, 7), (5, 7)])
    puzzle.add_arrow([(2, 0)], [(3, 0), (4, 1), (5, 2)])
    puzzle.add_arrow([(4, 4)], [(4, 5), (4, 6), (5, 6), (6, 5)])
    puzzle.add_arrow([(0, 2)], [(1, 3), (2, 4)])
    puzzle.add_arrow([(6, 2)], [(7, 2), (8, 2)])
    puzzle.add_arrow([(7, 1)], [(7, 0), (8, 1)])
    puzzle.add_arrow([(5, 0)], [(6, 0), (6, 1)])
    puzzle.add_arrow([(3, 1)], [(2, 1), (2, 2), (1, 2)])
    puzzle.add_arrow([(1, 0)], [(0, 1), (1, 1)])
    puzzle.add_arrow([(0, 8)], [(1, 8), (0, 7)])
    puzzle.add_arrow([(2, 5)], [(3, 4), (3, 3)])
    puzzle.add_arrow([(1, 5)], [(0, 4), (0, 5)])
    puzzle.add_arrow([(5, 4)], [(6, 4), (5, 5)])
    puzzle.add_arrow([(6, 6)], [(7, 7), (7, 8)])
    puzzle.add_arrow([(7, 5)], [(8, 5), (8, 4)])
    puzzle.add_arrow([(3, 8)], [(4, 7), (5, 8)])

    return puzzle
