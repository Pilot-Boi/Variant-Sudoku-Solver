"""PuzzleMadness Arrow Sudoku — 2025-04-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 8],
        [0, 0, 0, 5, 2, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 3)], [(7, 2), (7, 1)])
    puzzle.add_arrow([(3, 5)], [(4, 5), (4, 6)])
    puzzle.add_arrow([(1, 2)], [(2, 2), (3, 1), (3, 2)])
    puzzle.add_arrow([(7, 4)], [(8, 4), (8, 3)])
    puzzle.add_arrow([(3, 8)], [(3, 7), (4, 8), (4, 7)])
    puzzle.add_arrow([(4, 3)], [(5, 3), (5, 2), (6, 2)])
    puzzle.add_arrow([(7, 5)], [(7, 6), (8, 7), (7, 7)])
    puzzle.add_arrow([(1, 1)], [(1, 0), (2, 0)])
    puzzle.add_arrow([(1, 6)], [(0, 6), (1, 5), (2, 6)])
    puzzle.add_arrow([(2, 4)], [(1, 4), (0, 4), (0, 5)])
    puzzle.add_arrow([(6, 0)], [(5, 1), (4, 1)])
    puzzle.add_arrow([(6, 5)], [(6, 6), (5, 6)])
    puzzle.add_arrow([(1, 7)], [(0, 7), (1, 8)])
    puzzle.add_arrow([(5, 8)], [(6, 8), (5, 7)])
    puzzle.add_arrow([(3, 6)], [(2, 5), (3, 4)])
    puzzle.add_arrow([(8, 1)], [(7, 0), (6, 1)])
    puzzle.add_arrow([(0, 1)], [(0, 2), (1, 3)])

    return puzzle
