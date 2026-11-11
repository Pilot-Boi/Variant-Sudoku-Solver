"""PuzzleMadness Arrow Sudoku — 2025-09-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 2, 0, 1, 0, 7, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 2)], [(3, 2), (2, 3), (1, 4)])
    puzzle.add_arrow([(1, 1)], [(2, 2), (1, 2), (2, 1)])
    puzzle.add_arrow([(5, 5)], [(4, 5), (3, 5)])
    puzzle.add_arrow([(7, 3)], [(8, 2), (7, 1)])
    puzzle.add_arrow([(6, 5)], [(6, 6), (7, 5)])
    puzzle.add_arrow([(3, 3)], [(4, 4), (5, 4), (5, 3)])
    puzzle.add_arrow([(6, 8)], [(5, 7), (4, 6)])
    puzzle.add_arrow([(0, 5)], [(1, 6), (1, 7)])
    puzzle.add_arrow([(4, 0)], [(4, 1), (3, 1)])
    puzzle.add_arrow([(2, 7)], [(3, 8), (4, 8)])
    puzzle.add_arrow([(7, 6)], [(6, 7), (5, 8)])
    puzzle.add_arrow([(8, 0)], [(7, 0), (8, 1), (7, 2)])
    puzzle.add_arrow([(1, 5)], [(0, 4), (0, 3)])
    puzzle.add_arrow([(6, 2)], [(6, 3), (5, 2)])
    puzzle.add_arrow([(8, 4)], [(7, 4), (8, 5)])
    puzzle.add_arrow([(2, 8)], [(3, 7), (2, 6)])
    puzzle.add_arrow([(8, 7)], [(8, 8), (7, 8)])
    puzzle.add_arrow([(1, 8)], [(0, 8), (0, 7)])
    puzzle.add_arrow([(0, 0)], [(1, 0), (2, 0)])
    puzzle.add_arrow([(3, 4)], [(2, 5), (3, 6)])

    return puzzle
