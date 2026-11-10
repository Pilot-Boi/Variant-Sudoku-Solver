"""PuzzleMadness Arrow Sudoku — 2026-10-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2026-10-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2026/10/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 2, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(0, 3)], [(0, 4), (1, 4), (2, 4), (3, 3)])
    puzzle.add_arrow([(2, 3)], [(2, 2), (3, 1), (4, 2)])
    puzzle.add_arrow([(3, 5)], [(2, 6), (2, 7)])
    puzzle.add_arrow([(6, 6)], [(6, 5), (7, 6), (8, 6)])
    puzzle.add_arrow([(2, 5)], [(1, 6), (0, 5)])
    puzzle.add_arrow([(7, 1)], [(6, 1), (5, 1), (6, 0)])
    puzzle.add_arrow([(6, 7)], [(5, 7), (6, 8)])
    puzzle.add_arrow([(5, 4)], [(4, 5), (5, 6)])
    puzzle.add_arrow([(3, 6)], [(3, 7), (3, 8), (4, 8)])
    puzzle.add_arrow([(4, 4)], [(3, 4), (4, 3)])
    puzzle.add_arrow([(1, 1)], [(0, 2), (1, 2)])
    puzzle.add_arrow([(1, 7)], [(0, 7), (0, 8)])
    puzzle.add_arrow([(8, 4)], [(8, 3), (8, 2)])
    puzzle.add_arrow([(5, 2)], [(6, 3), (5, 3)])
    puzzle.add_arrow([(2, 1)], [(1, 0), (0, 0)])
    puzzle.add_arrow([(8, 7)], [(7, 8), (7, 7)])
    puzzle.add_arrow([(7, 5)], [(7, 4), (7, 3)])
    puzzle.add_arrow([(3, 0)], [(4, 1), (5, 0)])

    return puzzle
