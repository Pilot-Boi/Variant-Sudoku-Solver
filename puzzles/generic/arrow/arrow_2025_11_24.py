"""PuzzleMadness Arrow Sudoku — 2025-11-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 7, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 3)], [(6, 2), (7, 2)])
    puzzle.add_arrow([(4, 2)], [(3, 3), (2, 4), (1, 5), (2, 5)])
    puzzle.add_arrow([(1, 2)], [(1, 1), (2, 1)])
    puzzle.add_arrow([(7, 5)], [(7, 4), (7, 3), (8, 2)])
    puzzle.add_arrow([(4, 4)], [(5, 3), (5, 2)])
    puzzle.add_arrow([(2, 8)], [(1, 7), (1, 6), (0, 7)])
    puzzle.add_arrow([(4, 7)], [(5, 6), (5, 5)])
    puzzle.add_arrow([(3, 0)], [(4, 1), (4, 0), (5, 1)])
    puzzle.add_arrow([(7, 7)], [(7, 6), (6, 7)])
    puzzle.add_arrow([(2, 6)], [(3, 7), (4, 8)])
    puzzle.add_arrow([(2, 7)], [(3, 6), (4, 5)])
    puzzle.add_arrow([(0, 5)], [(1, 4), (0, 4)])
    puzzle.add_arrow([(2, 0)], [(1, 0), (0, 0)])
    puzzle.add_arrow([(7, 8)], [(6, 8), (5, 8)])
    puzzle.add_arrow([(1, 3)], [(2, 2), (3, 1)])

    return puzzle
