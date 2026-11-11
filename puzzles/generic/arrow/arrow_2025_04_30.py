"""PuzzleMadness Arrow Sudoku — 2025-04-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 9, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 7, 0, 9, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 6)], [(7, 5), (8, 5)])
    puzzle.add_arrow([(2, 2)], [(3, 3), (2, 4), (3, 5)])
    puzzle.add_arrow([(4, 4)], [(4, 3), (4, 2)])
    puzzle.add_arrow([(0, 7)], [(0, 8), (1, 7), (1, 8)])
    puzzle.add_arrow([(5, 2)], [(4, 1), (4, 0)])
    puzzle.add_arrow([(1, 2)], [(1, 1), (2, 0), (2, 1)])
    puzzle.add_arrow([(5, 6)], [(5, 7), (4, 6), (4, 7)])
    puzzle.add_arrow([(5, 5)], [(5, 4), (6, 5)])
    puzzle.add_arrow([(8, 7)], [(7, 7), (8, 8)])
    puzzle.add_arrow([(8, 0)], [(7, 1), (6, 0)])
    puzzle.add_arrow([(1, 4)], [(2, 3), (3, 2)])
    puzzle.add_arrow([(7, 4)], [(8, 3), (8, 2)])
    puzzle.add_arrow([(6, 3)], [(6, 2), (6, 1)])
    puzzle.add_arrow([(1, 5)], [(0, 6), (1, 6)])
    puzzle.add_arrow([(0, 2)], [(1, 3), (0, 4)])
    puzzle.add_arrow([(6, 8)], [(5, 8), (4, 8)])

    return puzzle
