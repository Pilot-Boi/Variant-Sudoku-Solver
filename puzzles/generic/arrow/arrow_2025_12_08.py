"""PuzzleMadness Arrow Sudoku — 2025-12-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-12-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/12/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 0, 8, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 0)], [(3, 1), (2, 2), (2, 1), (1, 0)])
    puzzle.add_arrow([(6, 1)], [(5, 0), (6, 0)])
    puzzle.add_arrow([(7, 3)], [(8, 3), (8, 4)])
    puzzle.add_arrow([(4, 5)], [(5, 6), (6, 5), (6, 4)])
    puzzle.add_arrow([(8, 7)], [(7, 6), (7, 7)])
    puzzle.add_arrow([(5, 2)], [(6, 2), (5, 3), (5, 4)])
    puzzle.add_arrow([(5, 8)], [(4, 8), (5, 7), (4, 6)])
    puzzle.add_arrow([(3, 2)], [(4, 2), (3, 3)])
    puzzle.add_arrow([(2, 3)], [(1, 3), (1, 4)])
    puzzle.add_arrow([(1, 6)], [(0, 6), (0, 5)])
    puzzle.add_arrow([(1, 7)], [(2, 8), (1, 8), (0, 8)])
    puzzle.add_arrow([(8, 1)], [(7, 2), (8, 2)])
    puzzle.add_arrow([(4, 4)], [(3, 4), (2, 5)])
    puzzle.add_arrow([(4, 7)], [(3, 8), (2, 7)])
    puzzle.add_arrow([(2, 0)], [(1, 1), (0, 1)])
    puzzle.add_arrow([(1, 5)], [(2, 4), (3, 5)])
    puzzle.add_arrow([(5, 5)], [(6, 6), (7, 5)])
    puzzle.add_arrow([(1, 2)], [(0, 3), (0, 2)])

    return puzzle
