"""PuzzleMadness Arrow Sudoku — 2025-01-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 9, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [6, 0, 0, 3, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 2)], [(2, 3), (2, 4), (1, 4)])
    puzzle.add_arrow([(5, 0)], [(6, 1), (6, 2), (5, 3), (6, 4)])
    puzzle.add_arrow([(7, 3)], [(8, 4), (8, 5)])
    puzzle.add_arrow([(6, 8)], [(6, 7), (7, 7)])
    puzzle.add_arrow([(2, 7)], [(2, 6), (3, 7), (4, 8)])
    puzzle.add_arrow([(2, 5)], [(1, 6), (0, 5)])
    puzzle.add_arrow([(2, 2)], [(2, 1), (2, 0), (1, 0)])
    puzzle.add_arrow([(0, 8)], [(1, 7), (0, 6)])
    puzzle.add_arrow([(7, 1)], [(6, 0), (7, 0)])
    puzzle.add_arrow([(3, 0)], [(3, 1), (4, 0)])
    puzzle.add_arrow([(3, 4)], [(3, 3), (4, 3)])
    puzzle.add_arrow([(6, 5)], [(7, 5), (7, 4)])
    puzzle.add_arrow([(0, 1)], [(0, 2), (0, 3)])
    puzzle.add_arrow([(4, 7)], [(3, 6), (3, 5)])
    puzzle.add_arrow([(4, 5)], [(4, 6), (5, 7)])
    puzzle.add_arrow([(8, 1)], [(8, 2), (8, 3)])

    return puzzle
