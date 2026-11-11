"""PuzzleMadness Arrow Sudoku — 2025-12-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-12-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/12/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 1)], [(5, 0), (6, 1), (6, 0)])
    puzzle.add_arrow([(3, 3)], [(3, 4), (4, 3), (4, 2)])
    puzzle.add_arrow([(8, 0)], [(7, 1), (7, 0)])
    puzzle.add_arrow([(2, 6)], [(1, 7), (0, 6)])
    puzzle.add_arrow([(7, 2)], [(8, 3), (7, 4), (7, 3), (6, 2)])
    puzzle.add_arrow([(7, 7)], [(8, 8), (8, 7), (8, 6)])
    puzzle.add_arrow([(2, 5)], [(1, 5), (2, 4)])
    puzzle.add_arrow([(3, 6)], [(2, 7), (2, 8), (3, 8)])
    puzzle.add_arrow([(4, 4)], [(5, 3), (6, 3)])
    puzzle.add_arrow([(1, 3)], [(1, 4), (0, 4), (0, 5)])
    puzzle.add_arrow([(5, 7)], [(6, 6), (6, 5), (5, 6)])
    puzzle.add_arrow([(1, 2)], [(0, 1), (0, 0)])
    puzzle.add_arrow([(0, 8)], [(0, 7), (1, 8)])
    puzzle.add_arrow([(5, 5)], [(4, 5), (4, 6)])
    puzzle.add_arrow([(3, 0)], [(3, 1), (2, 2)])
    puzzle.add_arrow([(0, 2)], [(1, 1), (2, 1)])

    return puzzle
