"""PuzzleMadness Arrow Sudoku — 2025-10-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 6)], [(7, 7), (8, 8)])
    puzzle.add_arrow([(1, 4)], [(0, 3), (1, 3), (1, 2), (0, 2)])
    puzzle.add_arrow([(3, 3)], [(4, 4), (3, 4)])
    puzzle.add_arrow([(2, 8)], [(2, 7), (1, 6)])
    puzzle.add_arrow([(5, 8)], [(6, 7), (7, 8), (6, 8)])
    puzzle.add_arrow([(2, 5)], [(3, 5), (3, 6)])
    puzzle.add_arrow([(5, 1)], [(4, 2), (4, 1), (5, 0)])
    puzzle.add_arrow([(8, 0)], [(7, 0), (6, 1), (6, 2)])
    puzzle.add_arrow([(0, 5)], [(0, 6), (1, 5), (2, 6), (3, 7)])
    puzzle.add_arrow([(8, 2)], [(8, 3), (7, 3), (8, 4)])
    puzzle.add_arrow([(5, 3)], [(6, 3), (7, 4)])
    puzzle.add_arrow([(2, 0)], [(1, 0), (0, 1)])
    puzzle.add_arrow([(4, 7)], [(4, 6), (4, 5)])
    puzzle.add_arrow([(6, 4)], [(5, 5), (5, 6)])
    puzzle.add_arrow([(3, 2)], [(2, 3), (2, 4)])
    puzzle.add_arrow([(8, 1)], [(7, 1), (6, 0)])

    return puzzle
