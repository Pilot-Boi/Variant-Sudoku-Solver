"""PuzzleMadness Arrow Sudoku — 2026-10-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2026-10-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2026/10/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 4)], [(5, 5), (4, 5)])
    puzzle.add_arrow([(4, 4)], [(5, 3), (5, 4)])
    puzzle.add_arrow([(6, 7)], [(7, 6), (6, 5)])
    puzzle.add_arrow([(5, 8)], [(5, 7), (4, 7), (3, 8)])
    puzzle.add_arrow([(3, 5)], [(2, 6), (1, 6), (2, 7)])
    puzzle.add_arrow([(4, 1)], [(3, 1), (2, 1), (3, 2)])
    puzzle.add_arrow([(1, 2)], [(0, 1), (1, 1)])
    puzzle.add_arrow([(1, 4)], [(0, 3), (1, 3)])
    puzzle.add_arrow([(8, 2)], [(8, 1), (8, 0)])
    puzzle.add_arrow([(5, 1)], [(6, 0), (5, 0)])
    puzzle.add_arrow([(6, 3)], [(7, 2), (6, 2), (7, 1)])
    puzzle.add_arrow([(3, 4)], [(2, 3), (2, 4)])
    puzzle.add_arrow([(7, 3)], [(8, 4), (8, 5)])
    puzzle.add_arrow([(6, 8)], [(7, 7), (7, 8)])
    puzzle.add_arrow([(4, 6)], [(3, 7), (4, 8)])
    puzzle.add_arrow([(7, 4)], [(7, 5), (6, 6)])
    puzzle.add_arrow([(0, 0)], [(1, 0), (2, 0)])
    puzzle.add_arrow([(0, 6)], [(0, 7), (0, 8)])

    return puzzle
