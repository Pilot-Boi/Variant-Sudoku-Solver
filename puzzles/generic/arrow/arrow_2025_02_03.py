"""PuzzleMadness Arrow Sudoku — 2025-02-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 5)], [(6, 4), (6, 5)])
    puzzle.add_arrow([(2, 0)], [(2, 1), (2, 2), (2, 3)])
    puzzle.add_arrow([(5, 7)], [(4, 6), (4, 5), (5, 6), (6, 7)])
    puzzle.add_arrow([(1, 8)], [(1, 7), (0, 7), (0, 6)])
    puzzle.add_arrow([(7, 4)], [(8, 4), (8, 5)])
    puzzle.add_arrow([(8, 2)], [(7, 1), (6, 1), (5, 0)])
    puzzle.add_arrow([(1, 6)], [(1, 5), (1, 4), (1, 3)])
    puzzle.add_arrow([(5, 3)], [(5, 2), (6, 3)])
    puzzle.add_arrow([(7, 7)], [(8, 6), (7, 5)])
    puzzle.add_arrow([(3, 6)], [(3, 5), (3, 4)])
    puzzle.add_arrow([(8, 0)], [(8, 1), (7, 2)])
    puzzle.add_arrow([(1, 1)], [(0, 1), (0, 2)])
    puzzle.add_arrow([(3, 8)], [(3, 7), (4, 8)])
    puzzle.add_arrow([(4, 3)], [(3, 2), (3, 3)])
    puzzle.add_arrow([(8, 7)], [(8, 8), (7, 8)])
    puzzle.add_arrow([(4, 1)], [(5, 1), (4, 0)])
    puzzle.add_arrow([(2, 5)], [(2, 6), (2, 7)])
    puzzle.add_arrow([(0, 4)], [(0, 3), (1, 2)])

    return puzzle
