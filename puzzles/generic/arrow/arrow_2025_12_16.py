"""PuzzleMadness Arrow Sudoku — 2025-12-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-12-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/12/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [4, 0, 0, 0, 0, 5, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 1)], [(4, 2), (5, 3), (6, 2), (6, 1)])
    puzzle.add_arrow([(1, 0)], [(0, 0), (0, 1), (1, 2), (2, 3)])
    puzzle.add_arrow([(0, 5)], [(1, 6), (1, 5), (2, 4), (3, 5)])
    puzzle.add_arrow([(6, 6)], [(6, 5), (5, 5)])
    puzzle.add_arrow([(7, 8)], [(6, 7), (5, 8)])
    puzzle.add_arrow([(6, 3)], [(7, 4), (7, 3), (6, 4)])
    puzzle.add_arrow([(2, 8)], [(1, 8), (0, 7), (0, 8)])
    puzzle.add_arrow([(6, 8)], [(7, 7), (7, 6)])
    puzzle.add_arrow([(8, 1)], [(7, 1), (7, 0)])
    puzzle.add_arrow([(2, 2)], [(1, 1), (2, 0)])
    puzzle.add_arrow([(4, 7)], [(5, 6), (4, 5)])
    puzzle.add_arrow([(3, 3)], [(3, 2), (4, 1)])
    puzzle.add_arrow([(5, 7)], [(4, 6), (3, 7)])
    puzzle.add_arrow([(5, 1)], [(5, 2), (4, 3)])
    puzzle.add_arrow([(2, 6)], [(2, 5), (3, 6)])
    puzzle.add_arrow([(5, 0)], [(4, 0), (3, 0)])

    return puzzle
