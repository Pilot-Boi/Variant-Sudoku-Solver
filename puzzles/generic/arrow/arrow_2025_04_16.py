"""PuzzleMadness Arrow Sudoku — 2025-04-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 4, 1, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 3)], [(6, 4), (6, 5), (5, 4)])
    puzzle.add_arrow([(4, 0)], [(3, 1), (4, 2), (4, 1)])
    puzzle.add_arrow([(6, 6)], [(5, 5), (5, 6), (6, 7), (7, 7)])
    puzzle.add_arrow([(1, 4)], [(0, 3), (0, 2)])
    puzzle.add_arrow([(4, 3)], [(4, 4), (3, 5), (4, 6)])
    puzzle.add_arrow([(7, 1)], [(8, 0), (7, 0), (8, 1)])
    puzzle.add_arrow([(0, 7)], [(0, 8), (1, 8)])
    puzzle.add_arrow([(8, 2)], [(8, 3), (7, 2), (6, 3)])
    puzzle.add_arrow([(2, 2)], [(1, 3), (2, 3)])
    puzzle.add_arrow([(3, 7)], [(2, 8), (2, 7)])
    puzzle.add_arrow([(0, 5)], [(1, 5), (0, 4)])
    puzzle.add_arrow([(0, 1)], [(1, 1), (2, 1)])
    puzzle.add_arrow([(8, 5)], [(8, 6), (8, 7)])
    puzzle.add_arrow([(4, 8)], [(5, 7), (5, 8)])
    puzzle.add_arrow([(2, 6)], [(1, 6), (0, 6)])

    return puzzle
