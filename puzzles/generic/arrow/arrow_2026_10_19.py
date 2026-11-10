"""PuzzleMadness Arrow Sudoku — 2026-10-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2026-10-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2026/10/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 3)], [(4, 2), (4, 3)])
    puzzle.add_arrow([(0, 4)], [(1, 3), (1, 2), (2, 1)])
    puzzle.add_arrow([(5, 8)], [(4, 7), (5, 6), (4, 6)])
    puzzle.add_arrow([(6, 3)], [(7, 3), (6, 4), (7, 5)])
    puzzle.add_arrow([(1, 0)], [(1, 1), (0, 1)])
    puzzle.add_arrow([(5, 2)], [(4, 1), (5, 0), (6, 1)])
    puzzle.add_arrow([(2, 5)], [(3, 5), (2, 4)])
    puzzle.add_arrow([(1, 8)], [(2, 7), (3, 7)])
    puzzle.add_arrow([(7, 7)], [(7, 8), (6, 7)])
    puzzle.add_arrow([(6, 2)], [(5, 3), (5, 4)])
    puzzle.add_arrow([(2, 6)], [(1, 7), (0, 6)])
    puzzle.add_arrow([(6, 5)], [(7, 6), (6, 6)])
    puzzle.add_arrow([(8, 5)], [(7, 4), (8, 3)])
    puzzle.add_arrow([(7, 0)], [(8, 1), (8, 2)])
    puzzle.add_arrow([(1, 6)], [(0, 5), (1, 5)])
    puzzle.add_arrow([(1, 4)], [(2, 3), (3, 2)])

    return puzzle
