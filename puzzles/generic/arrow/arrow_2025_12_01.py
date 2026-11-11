"""PuzzleMadness Arrow Sudoku — 2025-12-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-12-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/12/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 4, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 1],
        [0, 0, 0, 8, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 2)], [(5, 2), (4, 3), (3, 2), (2, 1)])
    puzzle.add_arrow([(8, 0)], [(7, 1), (8, 2)])
    puzzle.add_arrow([(3, 8)], [(3, 7), (4, 6)])
    puzzle.add_arrow([(1, 7)], [(0, 6), (0, 7)])
    puzzle.add_arrow([(3, 5)], [(2, 6), (1, 5), (0, 4)])
    puzzle.add_arrow([(7, 5)], [(7, 6), (6, 5), (6, 4)])
    puzzle.add_arrow([(1, 3)], [(1, 4), (2, 3)])
    puzzle.add_arrow([(6, 8)], [(7, 7), (8, 8), (7, 8)])
    puzzle.add_arrow([(5, 5)], [(4, 4), (3, 3), (2, 2)])
    puzzle.add_arrow([(0, 0)], [(1, 1), (2, 0)])
    puzzle.add_arrow([(8, 3)], [(7, 4), (8, 5)])
    puzzle.add_arrow([(4, 0)], [(5, 1), (5, 0)])
    puzzle.add_arrow([(4, 8)], [(4, 7), (5, 7), (6, 6)])
    puzzle.add_arrow([(8, 1)], [(7, 0), (6, 0)])
    puzzle.add_arrow([(2, 7)], [(1, 8), (0, 8)])
    puzzle.add_arrow([(3, 0)], [(3, 1), (4, 2)])

    return puzzle
