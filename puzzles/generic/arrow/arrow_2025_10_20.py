"""PuzzleMadness Arrow Sudoku — 2025-10-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 3, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 5)], [(2, 6), (1, 7), (2, 7)])
    puzzle.add_arrow([(6, 1)], [(5, 1), (4, 2), (5, 3), (5, 4)])
    puzzle.add_arrow([(3, 2)], [(2, 3), (3, 4), (2, 4)])
    puzzle.add_arrow([(2, 2)], [(3, 1), (4, 0)])
    puzzle.add_arrow([(7, 6)], [(8, 5), (7, 4)])
    puzzle.add_arrow([(2, 8)], [(3, 7), (3, 6)])
    puzzle.add_arrow([(8, 2)], [(8, 1), (7, 0), (6, 0)])
    puzzle.add_arrow([(1, 2)], [(1, 1), (0, 1)])
    puzzle.add_arrow([(6, 4)], [(6, 5), (5, 6)])
    puzzle.add_arrow([(4, 5)], [(4, 6), (4, 7)])
    puzzle.add_arrow([(1, 5)], [(1, 6), (0, 5), (1, 4)])
    puzzle.add_arrow([(8, 6)], [(7, 7), (7, 8)])
    puzzle.add_arrow([(8, 4)], [(7, 3), (7, 2)])
    puzzle.add_arrow([(4, 8)], [(5, 8), (6, 8)])
    puzzle.add_arrow([(4, 3)], [(4, 4), (3, 5)])
    puzzle.add_arrow([(6, 3)], [(5, 2), (6, 2)])
    puzzle.add_arrow([(0, 4)], [(1, 3), (0, 2)])

    return puzzle
