"""PuzzleMadness Arrow Sudoku — 2025-02-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [3, 6, 0, 0, 0, 8, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 5, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 5)], [(5, 6), (4, 6)])
    puzzle.add_arrow([(2, 7)], [(2, 8), (1, 7), (0, 7)])
    puzzle.add_arrow([(5, 0)], [(6, 1), (7, 1), (8, 1)])
    puzzle.add_arrow([(5, 4)], [(4, 4), (5, 3), (5, 2)])
    puzzle.add_arrow([(4, 2)], [(4, 1), (3, 1), (2, 0)])
    puzzle.add_arrow([(5, 8)], [(6, 8), (7, 7), (8, 8)])
    puzzle.add_arrow([(2, 3)], [(3, 3), (2, 2)])
    puzzle.add_arrow([(6, 4)], [(7, 4), (7, 3), (6, 2)])
    puzzle.add_arrow([(1, 3)], [(0, 4), (0, 5)])
    puzzle.add_arrow([(3, 4)], [(2, 5), (1, 4)])
    puzzle.add_arrow([(6, 5)], [(6, 6), (7, 5)])
    puzzle.add_arrow([(8, 3)], [(8, 4), (8, 5)])
    puzzle.add_arrow([(3, 7)], [(4, 7), (5, 7)])
    puzzle.add_arrow([(1, 5)], [(0, 6), (1, 6)])
    puzzle.add_arrow([(2, 1)], [(1, 1), (1, 0)])
    puzzle.add_arrow([(2, 6)], [(3, 5), (2, 4)])

    return puzzle
