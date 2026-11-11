"""PuzzleMadness Arrow Sudoku — 2025-10-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 9, 0, 3, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 5)], [(2, 6), (1, 6), (0, 6)])
    puzzle.add_arrow([(5, 5)], [(6, 5), (5, 4)])
    puzzle.add_arrow([(7, 0)], [(8, 0), (8, 1)])
    puzzle.add_arrow([(5, 1)], [(4, 0), (3, 0), (2, 1), (2, 2)])
    puzzle.add_arrow([(1, 2)], [(1, 3), (0, 4)])
    puzzle.add_arrow([(3, 4)], [(4, 5), (3, 6), (2, 7)])
    puzzle.add_arrow([(6, 2)], [(6, 3), (6, 4)])
    puzzle.add_arrow([(6, 8)], [(5, 7), (6, 7), (5, 8)])
    puzzle.add_arrow([(7, 7)], [(8, 7), (7, 6)])
    puzzle.add_arrow([(2, 3)], [(1, 4), (2, 4)])
    puzzle.add_arrow([(8, 3)], [(7, 3), (7, 2), (8, 2)])
    puzzle.add_arrow([(4, 2)], [(4, 1), (5, 0)])
    puzzle.add_arrow([(3, 3)], [(3, 2), (4, 3)])
    puzzle.add_arrow([(5, 2)], [(6, 1), (6, 0)])
    puzzle.add_arrow([(7, 4)], [(7, 5), (6, 6)])
    puzzle.add_arrow([(4, 6)], [(3, 5), (4, 4)])
    puzzle.add_arrow([(4, 7)], [(3, 7), (2, 8)])

    return puzzle
