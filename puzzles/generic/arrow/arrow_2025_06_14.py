"""PuzzleMadness Arrow Sudoku — 2025-06-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-06-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/6/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 7)], [(5, 6), (5, 5), (6, 4)])
    puzzle.add_arrow([(3, 1)], [(2, 2), (1, 3), (1, 4)])
    puzzle.add_arrow([(4, 8)], [(3, 7), (2, 6), (2, 7), (2, 8)])
    puzzle.add_arrow([(6, 0)], [(5, 1), (4, 1)])
    puzzle.add_arrow([(7, 6)], [(8, 6), (8, 7)])
    puzzle.add_arrow([(6, 6)], [(7, 5), (7, 4), (8, 3)])
    puzzle.add_arrow([(3, 4)], [(4, 5), (4, 4)])
    puzzle.add_arrow([(6, 7)], [(7, 8), (7, 7), (6, 8)])
    puzzle.add_arrow([(7, 1)], [(8, 0), (7, 0)])
    puzzle.add_arrow([(2, 5)], [(3, 6), (4, 6)])
    puzzle.add_arrow([(1, 1)], [(0, 2), (0, 1), (0, 0)])
    puzzle.add_arrow([(2, 4)], [(1, 5), (0, 4)])
    puzzle.add_arrow([(5, 2)], [(6, 2), (7, 3)])
    puzzle.add_arrow([(0, 6)], [(1, 7), (1, 8)])
    puzzle.add_arrow([(3, 3)], [(3, 2), (4, 3)])
    puzzle.add_arrow([(1, 0)], [(2, 1), (3, 0)])

    return puzzle
