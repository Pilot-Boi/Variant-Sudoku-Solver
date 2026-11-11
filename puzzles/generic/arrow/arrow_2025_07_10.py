"""PuzzleMadness Arrow Sudoku — 2025-07-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-07-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/7/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 5],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 4)], [(5, 4), (6, 3), (5, 3)])
    puzzle.add_arrow([(3, 0)], [(4, 1), (3, 1), (3, 2)])
    puzzle.add_arrow([(7, 8)], [(8, 7), (7, 7), (7, 6)])
    puzzle.add_arrow([(1, 1)], [(0, 1), (0, 0)])
    puzzle.add_arrow([(2, 3)], [(2, 2), (1, 3), (0, 3)])
    puzzle.add_arrow([(3, 5)], [(3, 6), (2, 7), (1, 6), (1, 5)])
    puzzle.add_arrow([(1, 2)], [(2, 1), (2, 0)])
    puzzle.add_arrow([(6, 1)], [(5, 1), (6, 0)])
    puzzle.add_arrow([(5, 5)], [(4, 5), (3, 4)])
    puzzle.add_arrow([(8, 2)], [(8, 1), (8, 0)])
    puzzle.add_arrow([(8, 5)], [(7, 5), (6, 6)])
    puzzle.add_arrow([(3, 7)], [(2, 8), (1, 7)])
    puzzle.add_arrow([(8, 3)], [(7, 4), (7, 3)])
    puzzle.add_arrow([(6, 7)], [(5, 8), (4, 8)])
    puzzle.add_arrow([(4, 7)], [(5, 7), (4, 6)])

    return puzzle
