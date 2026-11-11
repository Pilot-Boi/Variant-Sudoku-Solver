"""PuzzleMadness Arrow Sudoku — 2025-04-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 0, 0, 0, 5, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 1)], [(3, 1), (2, 2), (1, 2), (2, 3)])
    puzzle.add_arrow([(3, 5)], [(4, 6), (5, 7)])
    puzzle.add_arrow([(5, 5)], [(5, 6), (6, 7), (6, 6), (6, 5)])
    puzzle.add_arrow([(2, 7)], [(1, 8), (0, 8)])
    puzzle.add_arrow([(8, 5)], [(8, 4), (8, 3)])
    puzzle.add_arrow([(1, 6)], [(2, 5), (2, 4), (1, 5)])
    puzzle.add_arrow([(4, 2)], [(5, 3), (4, 4)])
    puzzle.add_arrow([(0, 0)], [(1, 0), (1, 1)])
    puzzle.add_arrow([(8, 6)], [(7, 7), (8, 7)])
    puzzle.add_arrow([(6, 2)], [(6, 1), (7, 0)])
    puzzle.add_arrow([(7, 1)], [(8, 1), (8, 0)])
    puzzle.add_arrow([(0, 4)], [(0, 5), (0, 6)])
    puzzle.add_arrow([(5, 4)], [(4, 3), (3, 4)])
    puzzle.add_arrow([(2, 8)], [(1, 7), (0, 7)])
    puzzle.add_arrow([(6, 8)], [(5, 8), (4, 8)])
    puzzle.add_arrow([(7, 3)], [(6, 3), (6, 4)])
    puzzle.add_arrow([(2, 0)], [(2, 1), (3, 2)])
    puzzle.add_arrow([(7, 4)], [(7, 5), (7, 6)])
    puzzle.add_arrow([(3, 0)], [(4, 0), (5, 1)])

    return puzzle
