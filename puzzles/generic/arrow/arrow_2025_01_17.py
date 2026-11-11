"""PuzzleMadness Arrow Sudoku — 2025-01-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 4, 0, 1, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 4)], [(6, 5), (7, 4), (8, 3)])
    puzzle.add_arrow([(2, 5)], [(3, 4), (3, 3)])
    puzzle.add_arrow([(5, 5)], [(5, 6), (5, 7)])
    puzzle.add_arrow([(2, 2)], [(1, 1), (1, 0), (2, 1)])
    puzzle.add_arrow([(3, 7)], [(3, 6), (2, 6)])
    puzzle.add_arrow([(8, 7)], [(7, 8), (7, 7)])
    puzzle.add_arrow([(2, 8)], [(2, 7), (1, 6)])
    puzzle.add_arrow([(7, 1)], [(6, 0), (7, 0), (6, 1)])
    puzzle.add_arrow([(5, 1)], [(4, 2), (3, 2), (3, 1)])
    puzzle.add_arrow([(0, 8)], [(0, 7), (1, 8)])
    puzzle.add_arrow([(0, 5)], [(1, 4), (2, 4)])
    puzzle.add_arrow([(7, 5)], [(8, 4), (8, 5)])
    puzzle.add_arrow([(0, 4)], [(0, 3), (1, 3)])
    puzzle.add_arrow([(5, 4)], [(4, 5), (4, 4)])
    puzzle.add_arrow([(6, 3)], [(5, 2), (6, 2)])
    puzzle.add_arrow([(0, 0)], [(0, 1), (1, 2)])
    puzzle.add_arrow([(6, 6)], [(6, 7), (6, 8)])
    puzzle.add_arrow([(3, 0)], [(4, 1), (4, 0)])

    return puzzle
