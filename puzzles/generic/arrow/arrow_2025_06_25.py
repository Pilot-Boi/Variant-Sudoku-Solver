"""PuzzleMadness Arrow Sudoku — 2025-06-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-06-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/6/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 3, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 5)], [(3, 6), (2, 6)])
    puzzle.add_arrow([(1, 5)], [(2, 4), (1, 3)])
    puzzle.add_arrow([(1, 2)], [(2, 1), (3, 2)])
    puzzle.add_arrow([(7, 4)], [(6, 5), (5, 4), (5, 3)])
    puzzle.add_arrow([(3, 7)], [(2, 8), (3, 8)])
    puzzle.add_arrow([(5, 0)], [(4, 0), (3, 0), (2, 0)])
    puzzle.add_arrow([(1, 7)], [(1, 8), (0, 7)])
    puzzle.add_arrow([(7, 8)], [(8, 7), (7, 6)])
    puzzle.add_arrow([(4, 8)], [(5, 8), (4, 7)])
    puzzle.add_arrow([(3, 1)], [(4, 2), (4, 3)])
    puzzle.add_arrow([(7, 1)], [(8, 2), (7, 2), (7, 3)])
    puzzle.add_arrow([(5, 1)], [(6, 2), (5, 2)])
    puzzle.add_arrow([(6, 8)], [(7, 7), (6, 6)])
    puzzle.add_arrow([(6, 3)], [(6, 4), (7, 5)])
    puzzle.add_arrow([(0, 2)], [(0, 1), (0, 0)])
    puzzle.add_arrow([(2, 5)], [(1, 4), (0, 3), (0, 4)])
    puzzle.add_arrow([(4, 6)], [(3, 5), (4, 4)])
    puzzle.add_arrow([(7, 0)], [(8, 0), (8, 1)])

    return puzzle
