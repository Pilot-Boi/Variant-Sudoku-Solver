"""PuzzleMadness Arrow Sudoku — 2025-04-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 7)], [(5, 6), (5, 5), (6, 4), (6, 5), (5, 4)])
    puzzle.add_arrow([(4, 4)], [(4, 5), (3, 6)])
    puzzle.add_arrow([(4, 2)], [(3, 3), (2, 2)])
    puzzle.add_arrow([(7, 1)], [(6, 2), (6, 1)])
    puzzle.add_arrow([(3, 0)], [(3, 1), (3, 2), (2, 3)])
    puzzle.add_arrow([(8, 3)], [(7, 3), (8, 2)])
    puzzle.add_arrow([(1, 1)], [(1, 2), (0, 1)])
    puzzle.add_arrow([(0, 6)], [(1, 7), (1, 6)])
    puzzle.add_arrow([(8, 5)], [(8, 4), (7, 5)])
    puzzle.add_arrow([(8, 7)], [(8, 6), (7, 6)])
    puzzle.add_arrow([(8, 8)], [(7, 8), (7, 7)])
    puzzle.add_arrow([(2, 8)], [(2, 7), (1, 8)])
    puzzle.add_arrow([(2, 4)], [(1, 4), (1, 3)])
    puzzle.add_arrow([(5, 2)], [(5, 1), (4, 1), (4, 0)])
    puzzle.add_arrow([(3, 8)], [(4, 8), (5, 7)])
    puzzle.add_arrow([(3, 5)], [(2, 6), (3, 7)])

    return puzzle
