"""PuzzleMadness Arrow Sudoku — 2025-03-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-03-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/3/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 7)], [(6, 6), (5, 5), (4, 6)])
    puzzle.add_arrow([(2, 1)], [(1, 2), (0, 2)])
    puzzle.add_arrow([(2, 3)], [(1, 4), (1, 5), (2, 4), (3, 3)])
    puzzle.add_arrow([(7, 4)], [(7, 3), (6, 4)])
    puzzle.add_arrow([(3, 8)], [(3, 7), (2, 7)])
    puzzle.add_arrow([(7, 5)], [(8, 4), (8, 3), (7, 2)])
    puzzle.add_arrow([(4, 1)], [(5, 0), (6, 1), (5, 1)])
    puzzle.add_arrow([(6, 3)], [(5, 2), (4, 3)])
    puzzle.add_arrow([(0, 6)], [(1, 6), (2, 6)])
    puzzle.add_arrow([(1, 0)], [(2, 0), (3, 0)])
    puzzle.add_arrow([(7, 7)], [(8, 8), (8, 7), (7, 8)])
    puzzle.add_arrow([(5, 4)], [(4, 5), (5, 6)])
    puzzle.add_arrow([(4, 4)], [(5, 3), (6, 2)])
    puzzle.add_arrow([(1, 3)], [(0, 3), (0, 4)])
    puzzle.add_arrow([(2, 8)], [(1, 7), (0, 8)])
    puzzle.add_arrow([(5, 8)], [(4, 7), (5, 7)])
    puzzle.add_arrow([(3, 2)], [(3, 1), (4, 2)])

    return puzzle
