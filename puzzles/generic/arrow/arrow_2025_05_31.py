"""PuzzleMadness Arrow Sudoku — 2025-05-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-05-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/5/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 8, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 6)], [(6, 5), (5, 5)])
    puzzle.add_arrow([(3, 1)], [(3, 2), (3, 3), (2, 3), (1, 4)])
    puzzle.add_arrow([(3, 4)], [(4, 5), (4, 6)])
    puzzle.add_arrow([(0, 7)], [(0, 6), (1, 7), (2, 7)])
    puzzle.add_arrow([(6, 1)], [(5, 1), (4, 0), (5, 0)])
    puzzle.add_arrow([(8, 7)], [(7, 7), (7, 6)])
    puzzle.add_arrow([(5, 7)], [(4, 8), (5, 8), (6, 8)])
    puzzle.add_arrow([(2, 8)], [(3, 8), (4, 7)])
    puzzle.add_arrow([(8, 2)], [(8, 1), (7, 1), (7, 0)])
    puzzle.add_arrow([(1, 1)], [(0, 2), (1, 3), (2, 2)])
    puzzle.add_arrow([(6, 3)], [(6, 4), (5, 4)])
    puzzle.add_arrow([(3, 6)], [(2, 6), (2, 5)])
    puzzle.add_arrow([(7, 3)], [(8, 4), (7, 4)])
    puzzle.add_arrow([(1, 0)], [(2, 1), (1, 2)])

    return puzzle
