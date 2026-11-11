"""PuzzleMadness Arrow Sudoku — 2025-08-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-08-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/8/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 3)], [(4, 4), (5, 5)])
    puzzle.add_arrow([(2, 4)], [(1, 3), (2, 2), (2, 1)])
    puzzle.add_arrow([(6, 5)], [(7, 4), (8, 5), (8, 4)])
    puzzle.add_arrow([(1, 0)], [(1, 1), (2, 0), (3, 1)])
    puzzle.add_arrow([(5, 7)], [(6, 6), (7, 6)])
    puzzle.add_arrow([(4, 3)], [(4, 2), (5, 2)])
    puzzle.add_arrow([(1, 8)], [(2, 7), (1, 7), (2, 6)])
    puzzle.add_arrow([(2, 5)], [(3, 6), (4, 5)])
    puzzle.add_arrow([(6, 0)], [(5, 1), (6, 2), (7, 2)])
    puzzle.add_arrow([(6, 1)], [(7, 0), (8, 0)])
    puzzle.add_arrow([(1, 4)], [(0, 3), (0, 4)])
    puzzle.add_arrow([(3, 7)], [(4, 8), (3, 8)])
    puzzle.add_arrow([(8, 6)], [(7, 7), (6, 8)])
    puzzle.add_arrow([(0, 8)], [(0, 7), (1, 6)])
    puzzle.add_arrow([(5, 8)], [(4, 7), (4, 6)])
    puzzle.add_arrow([(3, 0)], [(4, 0), (5, 0)])

    return puzzle
