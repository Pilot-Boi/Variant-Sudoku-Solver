"""PuzzleMadness Arrow Sudoku — 2025-07-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-07-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/7/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 2, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 2)], [(7, 3), (7, 2), (7, 1), (6, 0)])
    puzzle.add_arrow([(3, 5)], [(2, 6), (1, 7)])
    puzzle.add_arrow([(7, 8)], [(7, 7), (8, 8)])
    puzzle.add_arrow([(6, 6)], [(5, 6), (5, 7), (5, 8)])
    puzzle.add_arrow([(2, 4)], [(2, 3), (1, 4)])
    puzzle.add_arrow([(4, 0)], [(4, 1), (3, 0)])
    puzzle.add_arrow([(1, 1)], [(1, 2), (1, 3), (0, 4)])
    puzzle.add_arrow([(5, 3)], [(6, 4), (6, 3)])
    puzzle.add_arrow([(2, 0)], [(2, 1), (1, 0)])
    puzzle.add_arrow([(4, 4)], [(4, 3), (5, 4)])
    puzzle.add_arrow([(2, 5)], [(3, 4), (3, 3)])
    puzzle.add_arrow([(4, 2)], [(5, 1), (5, 0)])
    puzzle.add_arrow([(6, 5)], [(7, 6), (6, 7)])
    puzzle.add_arrow([(3, 8)], [(2, 7), (3, 6), (4, 5)])
    puzzle.add_arrow([(8, 6)], [(8, 5), (8, 4)])

    return puzzle
