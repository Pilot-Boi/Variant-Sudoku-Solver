"""PuzzleMadness Arrow Sudoku — 2025-04-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 6, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 2, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(8, 4)], [(7, 4), (6, 3)])
    puzzle.add_arrow([(6, 4)], [(5, 4), (6, 5)])
    puzzle.add_arrow([(4, 2)], [(3, 1), (2, 2), (2, 3)])
    puzzle.add_arrow([(2, 7)], [(2, 6), (1, 7), (2, 8)])
    puzzle.add_arrow([(1, 1)], [(0, 2), (0, 3), (1, 3)])
    puzzle.add_arrow([(5, 8)], [(4, 8), (5, 7), (6, 8)])
    puzzle.add_arrow([(3, 3)], [(4, 4), (3, 5)])
    puzzle.add_arrow([(7, 0)], [(7, 1), (8, 1)])
    puzzle.add_arrow([(3, 6)], [(4, 6), (4, 7)])
    puzzle.add_arrow([(7, 8)], [(6, 7), (7, 6), (8, 5)])
    puzzle.add_arrow([(8, 2)], [(7, 2), (6, 1)])
    puzzle.add_arrow([(5, 0)], [(4, 0), (4, 1)])
    puzzle.add_arrow([(5, 2)], [(5, 1), (6, 2)])
    puzzle.add_arrow([(2, 5)], [(1, 5), (1, 4)])
    puzzle.add_arrow([(6, 6)], [(5, 6), (5, 5)])
    puzzle.add_arrow([(2, 1)], [(1, 2), (0, 1)])

    return puzzle
