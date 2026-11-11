"""PuzzleMadness Arrow Sudoku — 2025-09-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 0)], [(3, 1), (3, 2)])
    puzzle.add_arrow([(2, 5)], [(2, 4), (3, 3)])
    puzzle.add_arrow([(7, 7)], [(8, 7), (8, 6), (7, 6)])
    puzzle.add_arrow([(1, 7)], [(2, 8), (3, 7)])
    puzzle.add_arrow([(7, 3)], [(7, 4), (6, 5), (5, 4)])
    puzzle.add_arrow([(4, 6)], [(3, 6), (4, 7)])
    puzzle.add_arrow([(7, 2)], [(6, 3), (5, 3), (4, 4)])
    puzzle.add_arrow([(1, 1)], [(2, 1), (1, 2), (0, 2)])
    puzzle.add_arrow([(5, 1)], [(6, 0), (7, 0)])
    puzzle.add_arrow([(0, 3)], [(0, 4), (1, 5)])
    puzzle.add_arrow([(6, 6)], [(7, 5), (8, 4)])
    puzzle.add_arrow([(4, 0)], [(4, 1), (4, 2)])
    puzzle.add_arrow([(1, 6)], [(0, 7), (0, 8)])
    puzzle.add_arrow([(6, 1)], [(7, 1), (8, 0)])
    puzzle.add_arrow([(3, 4)], [(2, 3), (1, 3)])
    puzzle.add_arrow([(5, 8)], [(6, 7), (5, 6)])

    return puzzle
