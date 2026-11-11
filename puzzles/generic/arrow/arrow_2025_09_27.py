"""PuzzleMadness Arrow Sudoku — 2025-09-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 3)], [(3, 2), (3, 3), (4, 4), (5, 3)])
    puzzle.add_arrow([(0, 6)], [(1, 6), (1, 7), (2, 7)])
    puzzle.add_arrow([(7, 0)], [(6, 0), (7, 1), (8, 0)])
    puzzle.add_arrow([(5, 2)], [(6, 3), (7, 4), (7, 5)])
    puzzle.add_arrow([(4, 1)], [(4, 2), (4, 3)])
    puzzle.add_arrow([(5, 8)], [(4, 7), (3, 7)])
    puzzle.add_arrow([(2, 2)], [(1, 1), (0, 1)])
    puzzle.add_arrow([(1, 4)], [(1, 5), (0, 5)])
    puzzle.add_arrow([(8, 3)], [(7, 2), (8, 2)])
    puzzle.add_arrow([(4, 5)], [(5, 4), (6, 5)])
    puzzle.add_arrow([(6, 2)], [(7, 3), (6, 4)])
    puzzle.add_arrow([(1, 3)], [(0, 3), (0, 4)])
    puzzle.add_arrow([(3, 5)], [(3, 6), (4, 6)])
    puzzle.add_arrow([(2, 0)], [(2, 1), (3, 1)])
    puzzle.add_arrow([(7, 7)], [(6, 7), (7, 6)])
    puzzle.add_arrow([(5, 7)], [(6, 8), (7, 8)])
    puzzle.add_arrow([(1, 8)], [(2, 8), (3, 8)])
    puzzle.add_arrow([(6, 1)], [(5, 0), (4, 0)])
    puzzle.add_arrow([(2, 4)], [(2, 5), (2, 6)])

    return puzzle
