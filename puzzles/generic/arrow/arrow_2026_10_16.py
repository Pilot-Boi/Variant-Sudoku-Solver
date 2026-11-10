"""PuzzleMadness Arrow Sudoku — 2026-10-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2026-10-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2026/10/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(0, 3)], [(1, 4), (1, 3)])
    puzzle.add_arrow([(4, 3)], [(4, 2), (3, 2)])
    puzzle.add_arrow([(8, 8)], [(8, 7), (7, 6), (7, 5)])
    puzzle.add_arrow([(5, 3)], [(6, 2), (7, 2), (8, 2)])
    puzzle.add_arrow([(7, 1)], [(6, 1), (5, 0), (4, 0)])
    puzzle.add_arrow([(4, 6)], [(5, 6), (4, 5), (3, 4)])
    puzzle.add_arrow([(3, 0)], [(2, 0), (2, 1), (3, 1)])
    puzzle.add_arrow([(4, 4)], [(5, 4), (6, 5), (6, 6)])
    puzzle.add_arrow([(3, 7)], [(2, 7), (2, 8), (3, 8)])
    puzzle.add_arrow([(6, 3)], [(7, 4), (8, 3), (7, 3)])
    puzzle.add_arrow([(0, 7)], [(1, 7), (1, 8)])
    puzzle.add_arrow([(2, 2)], [(2, 3), (3, 3)])
    puzzle.add_arrow([(0, 2)], [(1, 1), (0, 1), (0, 0)])
    puzzle.add_arrow([(0, 6)], [(1, 6), (0, 5)])
    puzzle.add_arrow([(5, 8)], [(4, 7), (4, 8)])

    return puzzle
