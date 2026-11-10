"""PuzzleMadness Arrow Sudoku — 2026-10-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2026-10-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2026/10/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [8, 5, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(8, 5)], [(7, 5), (6, 6), (6, 7)])
    puzzle.add_arrow([(0, 3)], [(1, 2), (1, 1), (0, 2)])
    puzzle.add_arrow([(5, 1)], [(5, 0), (4, 1), (3, 1)])
    puzzle.add_arrow([(2, 6)], [(2, 5), (3, 4), (2, 3), (1, 3)])
    puzzle.add_arrow([(4, 7)], [(4, 6), (5, 6), (6, 5)])
    puzzle.add_arrow([(7, 4)], [(6, 3), (7, 2)])
    puzzle.add_arrow([(2, 0)], [(3, 0), (4, 0)])
    puzzle.add_arrow([(7, 1)], [(7, 0), (8, 0)])
    puzzle.add_arrow([(5, 2)], [(5, 3), (4, 4)])
    puzzle.add_arrow([(1, 6)], [(2, 7), (1, 8)])
    puzzle.add_arrow([(0, 6)], [(0, 7), (0, 8)])
    puzzle.add_arrow([(3, 5)], [(3, 6), (4, 5)])
    puzzle.add_arrow([(0, 4)], [(1, 4), (2, 4)])
    puzzle.add_arrow([(3, 8)], [(2, 8), (1, 7)])
    puzzle.add_arrow([(8, 8)], [(8, 7), (8, 6)])
    puzzle.add_arrow([(8, 3)], [(7, 3), (6, 2)])
    puzzle.add_arrow([(6, 8)], [(7, 8), (7, 7)])
    puzzle.add_arrow([(3, 3)], [(4, 3), (5, 4)])

    return puzzle
