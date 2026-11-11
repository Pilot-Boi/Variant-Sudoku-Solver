"""PuzzleMadness Arrow Sudoku — 2025-05-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-05-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/5/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 6)], [(2, 5), (2, 4)])
    puzzle.add_arrow([(6, 5)], [(6, 6), (7, 5), (7, 4)])
    puzzle.add_arrow([(2, 6)], [(2, 7), (3, 8)])
    puzzle.add_arrow([(4, 7)], [(5, 7), (4, 8)])
    puzzle.add_arrow([(7, 0)], [(6, 0), (5, 0), (4, 0)])
    puzzle.add_arrow([(7, 2)], [(6, 2), (7, 1), (8, 2)])
    puzzle.add_arrow([(0, 3)], [(1, 4), (1, 5)])
    puzzle.add_arrow([(4, 2)], [(3, 1), (2, 2)])
    puzzle.add_arrow([(0, 0)], [(0, 1), (1, 2)])
    puzzle.add_arrow([(8, 8)], [(7, 8), (6, 8)])
    puzzle.add_arrow([(4, 3)], [(3, 4), (2, 3)])
    puzzle.add_arrow([(5, 6)], [(5, 5), (4, 6)])
    puzzle.add_arrow([(6, 3)], [(5, 2), (5, 3)])
    puzzle.add_arrow([(1, 7)], [(0, 7), (1, 8)])
    puzzle.add_arrow([(8, 3)], [(7, 3), (8, 4)])
    puzzle.add_arrow([(7, 7)], [(8, 6), (7, 6)])
    puzzle.add_arrow([(1, 1)], [(0, 2), (1, 3)])

    return puzzle
