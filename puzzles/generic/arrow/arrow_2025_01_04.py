"""PuzzleMadness Arrow Sudoku — 2025-01-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 5, 0],
        [0, 0, 1, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 2)], [(1, 3), (0, 3)])
    puzzle.add_arrow([(6, 5)], [(7, 4), (6, 4), (6, 3), (7, 2)])
    puzzle.add_arrow([(0, 8)], [(1, 7), (0, 7), (1, 8)])
    puzzle.add_arrow([(5, 3)], [(4, 2), (3, 1), (2, 1)])
    puzzle.add_arrow([(7, 8)], [(8, 7), (7, 7)])
    puzzle.add_arrow([(4, 3)], [(3, 4), (4, 5)])
    puzzle.add_arrow([(0, 1)], [(0, 0), (1, 0)])
    puzzle.add_arrow([(2, 4)], [(1, 5), (0, 4)])
    puzzle.add_arrow([(5, 2)], [(5, 1), (6, 1)])
    puzzle.add_arrow([(4, 8)], [(4, 7), (5, 8)])
    puzzle.add_arrow([(5, 5)], [(4, 6), (5, 6)])
    puzzle.add_arrow([(7, 0)], [(8, 1), (8, 0)])
    puzzle.add_arrow([(2, 7)], [(1, 6), (0, 5)])
    puzzle.add_arrow([(1, 1)], [(2, 2), (3, 2), (4, 1)])
    puzzle.add_arrow([(3, 3)], [(4, 4), (5, 4)])
    puzzle.add_arrow([(6, 7)], [(5, 7), (6, 8)])

    return puzzle
