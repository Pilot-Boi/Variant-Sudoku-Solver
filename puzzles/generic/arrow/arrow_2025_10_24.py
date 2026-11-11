"""PuzzleMadness Arrow Sudoku — 2025-10-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 4, 0, 6, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 4)], [(5, 5), (4, 4), (3, 3)])
    puzzle.add_arrow([(3, 6)], [(2, 6), (1, 5)])
    puzzle.add_arrow([(6, 6)], [(6, 5), (5, 6), (5, 7)])
    puzzle.add_arrow([(5, 3)], [(6, 2), (7, 3)])
    puzzle.add_arrow([(5, 2)], [(5, 1), (4, 0)])
    puzzle.add_arrow([(0, 5)], [(1, 6), (0, 6)])
    puzzle.add_arrow([(6, 8)], [(7, 8), (8, 8)])
    puzzle.add_arrow([(4, 8)], [(3, 8), (4, 7)])
    puzzle.add_arrow([(7, 1)], [(8, 2), (7, 2)])
    puzzle.add_arrow([(1, 2)], [(2, 2), (1, 3), (1, 4)])
    puzzle.add_arrow([(1, 1)], [(2, 0), (2, 1), (3, 0)])
    puzzle.add_arrow([(7, 6)], [(8, 6), (8, 5), (7, 4)])
    puzzle.add_arrow([(0, 3)], [(0, 2), (0, 1)])
    puzzle.add_arrow([(1, 8)], [(2, 8), (1, 7)])
    puzzle.add_arrow([(3, 2)], [(4, 2), (4, 3)])
    puzzle.add_arrow([(7, 0)], [(6, 0), (5, 0)])

    return puzzle
