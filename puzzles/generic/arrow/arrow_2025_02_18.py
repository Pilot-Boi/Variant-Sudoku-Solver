"""PuzzleMadness Arrow Sudoku — 2025-02-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 2],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(0, 4)], [(1, 5), (1, 6)])
    puzzle.add_arrow([(6, 7)], [(6, 6), (6, 5), (7, 4)])
    puzzle.add_arrow([(6, 0)], [(6, 1), (5, 2), (5, 3)])
    puzzle.add_arrow([(0, 8)], [(0, 7), (0, 6)])
    puzzle.add_arrow([(8, 0)], [(7, 1), (8, 2), (8, 3)])
    puzzle.add_arrow([(1, 7)], [(2, 6), (2, 7)])
    puzzle.add_arrow([(4, 5)], [(3, 4), (4, 4), (3, 5)])
    puzzle.add_arrow([(0, 2)], [(1, 1), (0, 1), (1, 0)])
    puzzle.add_arrow([(6, 2)], [(6, 3), (5, 4)])
    puzzle.add_arrow([(4, 3)], [(4, 2), (3, 2)])
    puzzle.add_arrow([(7, 7)], [(7, 8), (6, 8)])
    puzzle.add_arrow([(5, 8)], [(4, 8), (3, 8)])
    puzzle.add_arrow([(3, 6)], [(4, 7), (3, 7)])
    puzzle.add_arrow([(7, 5)], [(8, 5), (8, 6)])
    puzzle.add_arrow([(1, 2)], [(2, 3), (2, 2)])
    puzzle.add_arrow([(4, 1)], [(5, 0), (4, 0)])
    puzzle.add_arrow([(0, 5)], [(1, 4), (1, 3)])
    puzzle.add_arrow([(4, 6)], [(5, 6), (5, 5)])

    return puzzle
