"""PuzzleMadness Arrow Sudoku — 2025-12-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-12-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/12/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 5, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 8)], [(3, 7), (3, 6), (3, 5)])
    puzzle.add_arrow([(0, 2)], [(1, 3), (2, 3), (1, 2), (0, 3)])
    puzzle.add_arrow([(2, 1)], [(3, 2), (4, 3)])
    puzzle.add_arrow([(5, 3)], [(4, 2), (4, 1)])
    puzzle.add_arrow([(1, 7)], [(2, 8), (1, 8)])
    puzzle.add_arrow([(7, 6)], [(6, 7), (6, 8), (5, 8)])
    puzzle.add_arrow([(7, 2)], [(6, 1), (7, 1)])
    puzzle.add_arrow([(8, 7)], [(7, 7), (6, 6)])
    puzzle.add_arrow([(4, 6)], [(5, 6), (4, 5)])
    puzzle.add_arrow([(0, 1)], [(1, 1), (2, 0)])
    puzzle.add_arrow([(5, 5)], [(6, 5), (6, 4)])
    puzzle.add_arrow([(8, 3)], [(8, 2), (8, 1)])
    puzzle.add_arrow([(2, 5)], [(1, 6), (0, 6)])
    puzzle.add_arrow([(8, 6)], [(8, 5), (8, 4)])
    puzzle.add_arrow([(2, 4)], [(3, 4), (4, 4)])

    return puzzle
