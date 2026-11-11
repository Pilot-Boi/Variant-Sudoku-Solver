"""PuzzleMadness Arrow Sudoku — 2025-06-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-06-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/6/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 5, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 5)], [(1, 4), (2, 4)])
    puzzle.add_arrow([(0, 7)], [(1, 6), (2, 6)])
    puzzle.add_arrow([(5, 4)], [(5, 5), (4, 6)])
    puzzle.add_arrow([(7, 4)], [(6, 4), (7, 3)])
    puzzle.add_arrow([(7, 7)], [(6, 7), (6, 6), (5, 7)])
    puzzle.add_arrow([(5, 2)], [(5, 1), (6, 0), (7, 1)])
    puzzle.add_arrow([(2, 8)], [(3, 7), (3, 8)])
    puzzle.add_arrow([(4, 3)], [(4, 2), (4, 1)])
    puzzle.add_arrow([(2, 1)], [(1, 2), (1, 3), (2, 2)])
    puzzle.add_arrow([(1, 0)], [(2, 0), (3, 1)])
    puzzle.add_arrow([(6, 1)], [(7, 2), (8, 3)])
    puzzle.add_arrow([(4, 8)], [(5, 8), (6, 8)])
    puzzle.add_arrow([(3, 6)], [(4, 5), (3, 4), (4, 4)])
    puzzle.add_arrow([(1, 8)], [(1, 7), (0, 6)])

    return puzzle
