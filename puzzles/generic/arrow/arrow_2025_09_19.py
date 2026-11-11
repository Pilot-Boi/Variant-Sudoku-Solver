"""PuzzleMadness Arrow Sudoku — 2025-09-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 0)], [(3, 1), (4, 0)])
    puzzle.add_arrow([(4, 4)], [(3, 4), (4, 5), (3, 5)])
    puzzle.add_arrow([(1, 3)], [(0, 2), (1, 2)])
    puzzle.add_arrow([(3, 7)], [(2, 7), (2, 6)])
    puzzle.add_arrow([(4, 3)], [(5, 3), (5, 4)])
    puzzle.add_arrow([(6, 2)], [(7, 2), (7, 3), (7, 4), (6, 5)])
    puzzle.add_arrow([(6, 6)], [(6, 7), (5, 8), (4, 7)])
    puzzle.add_arrow([(8, 8)], [(8, 7), (8, 6)])
    puzzle.add_arrow([(1, 1)], [(2, 1), (2, 0), (1, 0)])
    puzzle.add_arrow([(7, 1)], [(8, 2), (8, 1), (8, 0)])
    puzzle.add_arrow([(1, 4)], [(2, 4), (1, 5)])
    puzzle.add_arrow([(6, 4)], [(6, 3), (5, 2)])
    puzzle.add_arrow([(5, 5)], [(4, 6), (5, 7)])
    puzzle.add_arrow([(8, 5)], [(7, 6), (7, 7)])
    puzzle.add_arrow([(7, 0)], [(6, 0), (5, 0)])
    puzzle.add_arrow([(0, 7)], [(1, 7), (0, 8)])
    puzzle.add_arrow([(4, 2)], [(4, 1), (3, 2)])
    puzzle.add_arrow([(1, 6)], [(0, 5), (0, 4)])

    return puzzle
