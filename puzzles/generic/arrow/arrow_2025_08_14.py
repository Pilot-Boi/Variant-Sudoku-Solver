"""PuzzleMadness Arrow Sudoku — 2025-08-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-08-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/8/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 5)], [(6, 4), (5, 4), (4, 3), (5, 3), (4, 2)])
    puzzle.add_arrow([(4, 7)], [(3, 7), (3, 6)])
    puzzle.add_arrow([(3, 3)], [(3, 2), (2, 1), (1, 2)])
    puzzle.add_arrow([(1, 6)], [(0, 5), (0, 6), (0, 7), (1, 7)])
    puzzle.add_arrow([(8, 2)], [(7, 1), (6, 0)])
    puzzle.add_arrow([(5, 7)], [(6, 7), (7, 6)])
    puzzle.add_arrow([(2, 5)], [(1, 5), (2, 6)])
    puzzle.add_arrow([(0, 4)], [(0, 3), (1, 4)])
    puzzle.add_arrow([(8, 3)], [(8, 4), (7, 3)])
    puzzle.add_arrow([(6, 6)], [(7, 7), (7, 8)])
    puzzle.add_arrow([(3, 0)], [(2, 0), (1, 0)])
    puzzle.add_arrow([(5, 1)], [(6, 2), (6, 3)])
    puzzle.add_arrow([(2, 8)], [(2, 7), (3, 8), (4, 8)])
    puzzle.add_arrow([(8, 1)], [(7, 2), (6, 1)])
    puzzle.add_arrow([(2, 2)], [(3, 1), (4, 0), (5, 0)])
    puzzle.add_arrow([(8, 8)], [(8, 7), (8, 6), (8, 5)])
    puzzle.add_arrow([(3, 5)], [(3, 4), (2, 3)])

    return puzzle
