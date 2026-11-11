"""PuzzleMadness Arrow Sudoku — 2025-10-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 4, 0, 0],
        [0, 0, 5, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(8, 6)], [(8, 5), (7, 5), (7, 4)])
    puzzle.add_arrow([(4, 5)], [(3, 4), (2, 3), (1, 3)])
    puzzle.add_arrow([(3, 1)], [(2, 1), (2, 2)])
    puzzle.add_arrow([(4, 3)], [(5, 4), (4, 4), (3, 3)])
    puzzle.add_arrow([(5, 3)], [(4, 2), (5, 2), (5, 1)])
    puzzle.add_arrow([(4, 6)], [(4, 7), (5, 7)])
    puzzle.add_arrow([(5, 0)], [(6, 1), (6, 2)])
    puzzle.add_arrow([(5, 6)], [(5, 5), (6, 6)])
    puzzle.add_arrow([(2, 7)], [(2, 6), (1, 5), (0, 6)])
    puzzle.add_arrow([(6, 0)], [(7, 0), (8, 0), (8, 1)])
    puzzle.add_arrow([(1, 1)], [(0, 1), (1, 2)])
    puzzle.add_arrow([(7, 7)], [(6, 8), (6, 7)])
    puzzle.add_arrow([(4, 0)], [(3, 0), (4, 1)])
    puzzle.add_arrow([(0, 8)], [(0, 7), (1, 7)])
    puzzle.add_arrow([(0, 2)], [(0, 3), (0, 4)])
    puzzle.add_arrow([(3, 6)], [(3, 7), (4, 8)])
    puzzle.add_arrow([(7, 2)], [(8, 3), (8, 4)])

    return puzzle
