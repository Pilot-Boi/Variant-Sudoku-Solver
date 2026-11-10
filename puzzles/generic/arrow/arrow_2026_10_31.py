"""PuzzleMadness Arrow Sudoku — 2026-10-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2026-10-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2026/10/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 4, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 2)], [(8, 1), (8, 2)])
    puzzle.add_arrow([(2, 3)], [(2, 4), (2, 5)])
    puzzle.add_arrow([(0, 2)], [(1, 1), (1, 2), (1, 3)])
    puzzle.add_arrow([(3, 3)], [(3, 2), (2, 1)])
    puzzle.add_arrow([(6, 1)], [(5, 0), (6, 0)])
    puzzle.add_arrow([(4, 7)], [(5, 7), (6, 7), (7, 7)])
    puzzle.add_arrow([(5, 3)], [(5, 2), (6, 2)])
    puzzle.add_arrow([(1, 4)], [(0, 3), (0, 4)])
    puzzle.add_arrow([(6, 5)], [(6, 6), (7, 6)])
    puzzle.add_arrow([(1, 5)], [(0, 6), (1, 6), (2, 7), (3, 7)])
    puzzle.add_arrow([(5, 4)], [(4, 4), (4, 5), (3, 5)])
    puzzle.add_arrow([(8, 0)], [(7, 1), (7, 0)])
    puzzle.add_arrow([(7, 3)], [(6, 3), (7, 4)])
    puzzle.add_arrow([(4, 1)], [(5, 1), (4, 0)])
    puzzle.add_arrow([(5, 8)], [(4, 8), (3, 8)])
    puzzle.add_arrow([(8, 6)], [(8, 5), (8, 4), (8, 3)])
    puzzle.add_arrow([(8, 7)], [(7, 8), (6, 8)])
    puzzle.add_arrow([(4, 2)], [(4, 3), (3, 4)])
    puzzle.add_arrow([(0, 8)], [(1, 7), (2, 8)])

    return puzzle
