"""PuzzleMadness Arrow Sudoku — 2025-12-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-12-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/12/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 3)], [(4, 3), (5, 2), (6, 3), (6, 2)])
    puzzle.add_arrow([(6, 0)], [(7, 0), (8, 0)])
    puzzle.add_arrow([(3, 4)], [(2, 5), (1, 5)])
    puzzle.add_arrow([(2, 2)], [(2, 1), (3, 1), (2, 0)])
    puzzle.add_arrow([(0, 6)], [(1, 7), (1, 8), (2, 7)])
    puzzle.add_arrow([(6, 6)], [(5, 6), (4, 6), (4, 7)])
    puzzle.add_arrow([(7, 5)], [(8, 5), (8, 6), (8, 7)])
    puzzle.add_arrow([(4, 5)], [(3, 5), (3, 6)])
    puzzle.add_arrow([(5, 5)], [(6, 4), (7, 3)])
    puzzle.add_arrow([(1, 1)], [(0, 2), (1, 2), (0, 1)])
    puzzle.add_arrow([(5, 1)], [(5, 0), (6, 1)])
    puzzle.add_arrow([(5, 7)], [(6, 8), (7, 8)])
    puzzle.add_arrow([(0, 7)], [(1, 6), (0, 5)])
    puzzle.add_arrow([(8, 3)], [(8, 2), (8, 1)])

    return puzzle
