"""PuzzleMadness Arrow Sudoku — 2025-04-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 9, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(0, 4)], [(0, 5), (0, 6)])
    puzzle.add_arrow([(8, 4)], [(8, 5), (8, 6)])
    puzzle.add_arrow([(1, 8)], [(2, 7), (2, 6), (1, 5)])
    puzzle.add_arrow([(3, 2)], [(2, 3), (3, 4), (4, 3), (5, 2)])
    puzzle.add_arrow([(0, 3)], [(1, 3), (1, 4)])
    puzzle.add_arrow([(4, 4)], [(5, 4), (6, 3), (7, 2)])
    puzzle.add_arrow([(6, 6)], [(6, 5), (6, 4)])
    puzzle.add_arrow([(3, 1)], [(2, 1), (1, 0), (0, 1)])
    puzzle.add_arrow([(3, 6)], [(4, 7), (5, 8), (4, 8)])
    puzzle.add_arrow([(6, 8)], [(7, 7), (8, 8), (7, 8)])
    puzzle.add_arrow([(0, 0)], [(1, 1), (0, 2)])
    puzzle.add_arrow([(7, 1)], [(6, 0), (7, 0)])
    puzzle.add_arrow([(2, 0)], [(3, 0), (4, 0)])
    puzzle.add_arrow([(5, 3)], [(6, 2), (5, 1)])
    puzzle.add_arrow([(1, 6)], [(1, 7), (0, 7)])
    puzzle.add_arrow([(8, 1)], [(8, 2), (8, 3)])

    return puzzle
