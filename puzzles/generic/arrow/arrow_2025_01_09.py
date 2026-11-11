"""PuzzleMadness Arrow Sudoku — 2025-01-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 5, 0, 0, 0, 0, 6, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 5)], [(8, 4), (8, 5), (7, 6), (6, 6)])
    puzzle.add_arrow([(7, 3)], [(6, 3), (6, 4)])
    puzzle.add_arrow([(3, 6)], [(3, 7), (2, 7), (1, 7)])
    puzzle.add_arrow([(4, 1)], [(3, 1), (2, 2), (1, 3)])
    puzzle.add_arrow([(5, 2)], [(6, 1), (7, 0)])
    puzzle.add_arrow([(4, 4)], [(5, 4), (4, 3)])
    puzzle.add_arrow([(5, 8)], [(4, 8), (4, 7), (3, 8)])
    puzzle.add_arrow([(0, 0)], [(1, 0), (0, 1)])
    puzzle.add_arrow([(7, 7)], [(8, 8), (8, 7)])
    puzzle.add_arrow([(6, 2)], [(7, 2), (7, 1)])
    puzzle.add_arrow([(1, 4)], [(1, 5), (0, 5)])
    puzzle.add_arrow([(3, 3)], [(2, 3), (3, 4), (4, 5)])
    puzzle.add_arrow([(5, 7)], [(5, 6), (6, 7)])
    puzzle.add_arrow([(4, 2)], [(3, 2), (2, 1)])
    puzzle.add_arrow([(5, 5)], [(6, 5), (7, 4)])
    puzzle.add_arrow([(6, 0)], [(5, 1), (4, 0)])

    return puzzle
