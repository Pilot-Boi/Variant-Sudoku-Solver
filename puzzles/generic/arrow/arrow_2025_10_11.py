"""PuzzleMadness Arrow Sudoku — 2025-10-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 4, 0, 1, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 2)], [(1, 1), (2, 1), (1, 2), (0, 3)])
    puzzle.add_arrow([(8, 1)], [(7, 2), (8, 3), (8, 2)])
    puzzle.add_arrow([(7, 5)], [(7, 6), (6, 7), (7, 7)])
    puzzle.add_arrow([(5, 4)], [(5, 5), (6, 4), (6, 5)])
    puzzle.add_arrow([(4, 4)], [(3, 5), (2, 6)])
    puzzle.add_arrow([(0, 0)], [(0, 1), (0, 2)])
    puzzle.add_arrow([(1, 3)], [(2, 4), (2, 3), (3, 3)])
    puzzle.add_arrow([(8, 7)], [(8, 8), (7, 8)])
    puzzle.add_arrow([(3, 1)], [(4, 2), (5, 3)])
    puzzle.add_arrow([(4, 7)], [(5, 7), (4, 8), (5, 8)])
    puzzle.add_arrow([(0, 8)], [(0, 7), (1, 7)])
    puzzle.add_arrow([(6, 0)], [(7, 0), (6, 1)])
    puzzle.add_arrow([(0, 5)], [(1, 6), (0, 6)])
    puzzle.add_arrow([(2, 7)], [(2, 8), (3, 8)])
    puzzle.add_arrow([(7, 3)], [(7, 4), (8, 4)])
    puzzle.add_arrow([(4, 1)], [(4, 0), (5, 0)])
    puzzle.add_arrow([(2, 5)], [(1, 4), (0, 4)])

    return puzzle
