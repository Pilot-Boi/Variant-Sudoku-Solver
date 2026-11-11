"""PuzzleMadness Arrow Sudoku — 2025-02-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 0, 2, 0],
        [0, 0, 0, 4, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 3)], [(3, 4), (2, 3), (2, 2), (1, 2)])
    puzzle.add_arrow([(7, 6)], [(6, 7), (6, 6)])
    puzzle.add_arrow([(6, 4)], [(5, 4), (4, 4)])
    puzzle.add_arrow([(2, 1)], [(3, 0), (3, 1)])
    puzzle.add_arrow([(4, 6)], [(4, 7), (5, 6)])
    puzzle.add_arrow([(6, 0)], [(6, 1), (6, 2), (6, 3)])
    puzzle.add_arrow([(8, 7)], [(8, 6), (7, 5)])
    puzzle.add_arrow([(2, 4)], [(1, 4), (1, 5)])
    puzzle.add_arrow([(7, 1)], [(8, 2), (8, 3)])
    puzzle.add_arrow([(3, 8)], [(2, 8), (2, 7)])
    puzzle.add_arrow([(0, 0)], [(1, 1), (0, 1), (1, 0)])
    puzzle.add_arrow([(3, 6)], [(2, 6), (3, 5)])
    puzzle.add_arrow([(1, 7)], [(0, 6), (0, 7), (0, 8)])
    puzzle.add_arrow([(8, 4)], [(7, 4), (6, 5)])
    puzzle.add_arrow([(0, 2)], [(1, 3), (0, 3)])
    puzzle.add_arrow([(5, 1)], [(4, 0), (4, 1)])
    puzzle.add_arrow([(7, 7)], [(6, 8), (5, 7)])

    return puzzle
