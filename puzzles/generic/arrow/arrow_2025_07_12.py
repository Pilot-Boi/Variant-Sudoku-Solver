"""PuzzleMadness Arrow Sudoku — 2025-07-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-07-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/7/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 1, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 0)], [(2, 0), (2, 1), (1, 0)])
    puzzle.add_arrow([(7, 3)], [(6, 2), (5, 2), (6, 3), (7, 4)])
    puzzle.add_arrow([(0, 4)], [(1, 5), (0, 6), (0, 7)])
    puzzle.add_arrow([(3, 4)], [(2, 5), (3, 6), (4, 6)])
    puzzle.add_arrow([(7, 5)], [(8, 6), (7, 6), (7, 7)])
    puzzle.add_arrow([(4, 3)], [(3, 3), (4, 2), (5, 3), (6, 4)])
    puzzle.add_arrow([(6, 1)], [(7, 0), (7, 1)])
    puzzle.add_arrow([(4, 7)], [(5, 7), (6, 6)])
    puzzle.add_arrow([(2, 6)], [(3, 5), (4, 4)])
    puzzle.add_arrow([(3, 1)], [(4, 1), (3, 2)])
    puzzle.add_arrow([(3, 7)], [(3, 8), (4, 8)])
    puzzle.add_arrow([(0, 1)], [(1, 1), (0, 0)])
    puzzle.add_arrow([(2, 7)], [(1, 7), (1, 8)])
    puzzle.add_arrow([(1, 3)], [(1, 4), (0, 5)])
    puzzle.add_arrow([(6, 7)], [(7, 8), (8, 8)])

    return puzzle
