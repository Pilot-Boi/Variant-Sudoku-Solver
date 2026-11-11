"""PuzzleMadness Arrow Sudoku — 2025-01-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 1, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 1],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 4)], [(7, 5), (6, 5)])
    puzzle.add_arrow([(5, 3)], [(5, 4), (5, 5), (4, 6), (4, 5)])
    puzzle.add_arrow([(0, 8)], [(1, 8), (0, 7)])
    puzzle.add_arrow([(3, 3)], [(2, 2), (3, 2), (4, 3)])
    puzzle.add_arrow([(2, 3)], [(1, 4), (0, 5)])
    puzzle.add_arrow([(6, 2)], [(5, 1), (5, 2)])
    puzzle.add_arrow([(7, 7)], [(6, 6), (5, 6)])
    puzzle.add_arrow([(7, 2)], [(7, 1), (7, 0)])
    puzzle.add_arrow([(0, 3)], [(0, 4), (1, 3)])
    puzzle.add_arrow([(3, 1)], [(2, 1), (1, 0)])
    puzzle.add_arrow([(6, 7)], [(7, 8), (8, 7)])
    puzzle.add_arrow([(2, 5)], [(2, 6), (1, 7)])
    puzzle.add_arrow([(8, 2)], [(7, 3), (8, 3)])
    puzzle.add_arrow([(2, 8)], [(3, 7), (3, 8)])
    puzzle.add_arrow([(4, 1)], [(3, 0), (2, 0)])
    puzzle.add_arrow([(0, 0)], [(1, 1), (0, 2)])

    return puzzle
