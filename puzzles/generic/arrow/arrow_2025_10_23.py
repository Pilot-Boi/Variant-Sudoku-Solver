"""PuzzleMadness Arrow Sudoku — 2025-10-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 9, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 1)], [(5, 2), (6, 1), (7, 1)])
    puzzle.add_arrow([(1, 6)], [(2, 7), (3, 6), (3, 5)])
    puzzle.add_arrow([(6, 6)], [(5, 5), (4, 6), (5, 6)])
    puzzle.add_arrow([(4, 3)], [(3, 4), (2, 3), (3, 2)])
    puzzle.add_arrow([(0, 4)], [(0, 3), (1, 2)])
    puzzle.add_arrow([(7, 2)], [(7, 3), (8, 3)])
    puzzle.add_arrow([(8, 7)], [(7, 6), (6, 7)])
    puzzle.add_arrow([(3, 1)], [(4, 0), (5, 0)])
    puzzle.add_arrow([(1, 1)], [(1, 0), (0, 1)])
    puzzle.add_arrow([(2, 8)], [(1, 7), (0, 6)])
    puzzle.add_arrow([(3, 3)], [(2, 4), (2, 5)])
    puzzle.add_arrow([(3, 8)], [(4, 8), (4, 7)])
    puzzle.add_arrow([(7, 5)], [(6, 4), (6, 5)])
    puzzle.add_arrow([(7, 4)], [(8, 5), (8, 6)])
    puzzle.add_arrow([(6, 0)], [(7, 0), (8, 1)])
    puzzle.add_arrow([(5, 8)], [(6, 8), (7, 8), (8, 8)])
    puzzle.add_arrow([(5, 4)], [(4, 4), (5, 3)])

    return puzzle
