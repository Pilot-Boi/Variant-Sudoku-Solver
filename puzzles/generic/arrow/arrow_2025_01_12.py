"""PuzzleMadness Arrow Sudoku — 2025-01-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(0, 1)], [(1, 2), (1, 3)])
    puzzle.add_arrow([(1, 4)], [(0, 3), (0, 4)])
    puzzle.add_arrow([(7, 3)], [(6, 4), (5, 5), (4, 5)])
    puzzle.add_arrow([(6, 7)], [(7, 8), (8, 7)])
    puzzle.add_arrow([(2, 5)], [(2, 6), (3, 5), (4, 4)])
    puzzle.add_arrow([(3, 3)], [(2, 2), (3, 1), (4, 1), (5, 0)])
    puzzle.add_arrow([(4, 8)], [(3, 7), (4, 7), (5, 7)])
    puzzle.add_arrow([(0, 7)], [(1, 8), (0, 8)])
    puzzle.add_arrow([(8, 0)], [(7, 1), (6, 1), (6, 2)])
    puzzle.add_arrow([(0, 5)], [(0, 6), (1, 6)])
    puzzle.add_arrow([(6, 6)], [(7, 5), (8, 5), (8, 4)])
    puzzle.add_arrow([(2, 1)], [(1, 1), (0, 0)])
    puzzle.add_arrow([(7, 6)], [(7, 7), (8, 8)])
    puzzle.add_arrow([(4, 6)], [(5, 6), (6, 5)])
    puzzle.add_arrow([(2, 8)], [(2, 7), (1, 7)])

    return puzzle
