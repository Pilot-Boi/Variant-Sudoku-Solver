"""PuzzleMadness Arrow Sudoku — 2026-10-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2026-10-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2026/10/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 9, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 6)], [(3, 7), (4, 6), (5, 5)])
    puzzle.add_arrow([(8, 4)], [(7, 5), (6, 6)])
    puzzle.add_arrow([(8, 1)], [(7, 1), (6, 1), (7, 2)])
    puzzle.add_arrow([(6, 2)], [(7, 3), (8, 2)])
    puzzle.add_arrow([(5, 0)], [(4, 1), (3, 1)])
    puzzle.add_arrow([(5, 2)], [(5, 3), (6, 4)])
    puzzle.add_arrow([(1, 6)], [(0, 5), (1, 4)])
    puzzle.add_arrow([(0, 0)], [(1, 0), (0, 1)])
    puzzle.add_arrow([(2, 4)], [(3, 3), (2, 2), (2, 1), (3, 0)])
    puzzle.add_arrow([(7, 6)], [(8, 6), (7, 7)])
    puzzle.add_arrow([(1, 7)], [(0, 6), (0, 7)])
    puzzle.add_arrow([(4, 5)], [(5, 6), (6, 5)])
    puzzle.add_arrow([(0, 4)], [(0, 3), (1, 3)])
    puzzle.add_arrow([(5, 8)], [(6, 7), (5, 7)])
    puzzle.add_arrow([(0, 8)], [(1, 8), (2, 8), (2, 7)])
    puzzle.add_arrow([(3, 6)], [(3, 5), (4, 4)])
    puzzle.add_arrow([(6, 3)], [(7, 4), (8, 5)])

    return puzzle
