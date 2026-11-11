"""PuzzleMadness Arrow Sudoku — 2025-05-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-05-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/5/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 1)], [(6, 2), (7, 3), (6, 3)])
    puzzle.add_arrow([(6, 5)], [(5, 5), (4, 6), (3, 7)])
    puzzle.add_arrow([(7, 8)], [(8, 7), (8, 8)])
    puzzle.add_arrow([(0, 0)], [(0, 1), (1, 2)])
    puzzle.add_arrow([(1, 4)], [(2, 4), (3, 4)])
    puzzle.add_arrow([(0, 6)], [(0, 7), (1, 6), (1, 7)])
    puzzle.add_arrow([(6, 7)], [(7, 6), (8, 6)])
    puzzle.add_arrow([(8, 1)], [(8, 2), (7, 1), (7, 2)])
    puzzle.add_arrow([(4, 7)], [(5, 7), (4, 8)])
    puzzle.add_arrow([(1, 3)], [(0, 2), (0, 3)])
    puzzle.add_arrow([(8, 5)], [(7, 5), (6, 4)])
    puzzle.add_arrow([(2, 6)], [(3, 6), (4, 5)])
    puzzle.add_arrow([(3, 5)], [(2, 5), (1, 5)])
    puzzle.add_arrow([(4, 2)], [(3, 3), (2, 2)])
    puzzle.add_arrow([(3, 2)], [(4, 1), (4, 0), (5, 1)])
    puzzle.add_arrow([(7, 7)], [(6, 8), (5, 8)])
    puzzle.add_arrow([(4, 3)], [(4, 4), (5, 4)])
    puzzle.add_arrow([(1, 0)], [(1, 1), (2, 0)])

    return puzzle
