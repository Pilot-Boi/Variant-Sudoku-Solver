"""PuzzleMadness Arrow Sudoku — 2025-11-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 5, 7, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 4)], [(6, 4), (7, 5), (8, 5), (8, 6)])
    puzzle.add_arrow([(3, 4)], [(2, 4), (3, 3), (4, 3), (5, 3)])
    puzzle.add_arrow([(6, 5)], [(5, 6), (5, 7)])
    puzzle.add_arrow([(6, 0)], [(7, 1), (6, 1), (7, 0)])
    puzzle.add_arrow([(0, 0)], [(0, 1), (1, 2)])
    puzzle.add_arrow([(3, 5)], [(3, 6), (2, 7)])
    puzzle.add_arrow([(2, 2)], [(3, 2), (4, 1)])
    puzzle.add_arrow([(1, 6)], [(1, 5), (1, 4)])
    puzzle.add_arrow([(8, 7)], [(7, 7), (6, 8)])
    puzzle.add_arrow([(7, 3)], [(8, 3), (7, 2)])
    puzzle.add_arrow([(3, 1)], [(2, 0), (1, 0), (1, 1)])
    puzzle.add_arrow([(5, 1)], [(4, 0), (5, 0)])
    puzzle.add_arrow([(2, 6)], [(1, 7), (0, 8)])
    puzzle.add_arrow([(7, 6)], [(6, 7), (5, 8)])
    puzzle.add_arrow([(1, 3)], [(0, 3), (0, 4)])

    return puzzle
