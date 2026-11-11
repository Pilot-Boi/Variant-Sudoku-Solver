"""PuzzleMadness Arrow Sudoku — 2025-11-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 3)], [(4, 4), (4, 3)])
    puzzle.add_arrow([(1, 6)], [(1, 5), (2, 4)])
    puzzle.add_arrow([(3, 4)], [(2, 5), (3, 5), (4, 6)])
    puzzle.add_arrow([(4, 0)], [(3, 0), (2, 0)])
    puzzle.add_arrow([(0, 2)], [(1, 3), (2, 2), (1, 1)])
    puzzle.add_arrow([(8, 2)], [(7, 3), (6, 4), (5, 4)])
    puzzle.add_arrow([(4, 1)], [(5, 1), (5, 2)])
    puzzle.add_arrow([(8, 7)], [(7, 8), (7, 7)])
    puzzle.add_arrow([(2, 8)], [(3, 8), (2, 7), (2, 6)])
    puzzle.add_arrow([(7, 2)], [(7, 1), (7, 0)])
    puzzle.add_arrow([(7, 6)], [(8, 6), (7, 5)])
    puzzle.add_arrow([(3, 1)], [(3, 2), (4, 2)])
    puzzle.add_arrow([(5, 5)], [(6, 5), (5, 6)])
    puzzle.add_arrow([(1, 8)], [(0, 7), (1, 7)])
    puzzle.add_arrow([(4, 7)], [(5, 8), (6, 7)])
    puzzle.add_arrow([(8, 5)], [(8, 4), (7, 4)])
    puzzle.add_arrow([(6, 3)], [(6, 2), (6, 1), (5, 0)])

    return puzzle
