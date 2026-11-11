"""PuzzleMadness Arrow Sudoku — 2025-02-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 2, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 4)], [(2, 5), (1, 5), (0, 5)])
    puzzle.add_arrow([(3, 0)], [(2, 1), (3, 1), (3, 2)])
    puzzle.add_arrow([(6, 2)], [(6, 1), (5, 1), (4, 0)])
    puzzle.add_arrow([(5, 6)], [(5, 7), (6, 6)])
    puzzle.add_arrow([(7, 1)], [(6, 0), (5, 0)])
    puzzle.add_arrow([(2, 8)], [(3, 8), (4, 7), (4, 6)])
    puzzle.add_arrow([(1, 6)], [(2, 6), (1, 7)])
    puzzle.add_arrow([(8, 5)], [(7, 5), (7, 4), (8, 3)])
    puzzle.add_arrow([(0, 1)], [(1, 1), (2, 2)])
    puzzle.add_arrow([(4, 3)], [(5, 4), (6, 4), (7, 3)])
    puzzle.add_arrow([(2, 4)], [(1, 3), (0, 2)])
    puzzle.add_arrow([(1, 8)], [(0, 7), (0, 6)])
    puzzle.add_arrow([(7, 7)], [(7, 6), (8, 7)])
    puzzle.add_arrow([(3, 3)], [(3, 4), (3, 5)])
    puzzle.add_arrow([(8, 1)], [(7, 0), (8, 0)])
    puzzle.add_arrow([(6, 8)], [(5, 8), (4, 8)])

    return puzzle
