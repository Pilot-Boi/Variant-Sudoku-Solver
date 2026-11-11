"""PuzzleMadness Arrow Sudoku — 2025-02-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 3, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 7)], [(3, 6), (4, 7), (5, 6)])
    puzzle.add_arrow([(3, 1)], [(4, 2), (5, 1), (6, 2)])
    puzzle.add_arrow([(8, 2)], [(7, 1), (7, 2)])
    puzzle.add_arrow([(7, 5)], [(6, 5), (7, 4)])
    puzzle.add_arrow([(1, 3)], [(0, 4), (0, 5)])
    puzzle.add_arrow([(1, 6)], [(2, 5), (1, 5)])
    puzzle.add_arrow([(0, 1)], [(1, 1), (2, 0)])
    puzzle.add_arrow([(4, 3)], [(3, 2), (2, 1), (1, 0)])
    puzzle.add_arrow([(6, 6)], [(5, 5), (6, 4)])
    puzzle.add_arrow([(8, 5)], [(8, 6), (8, 7), (7, 8)])
    puzzle.add_arrow([(4, 8)], [(5, 7), (6, 7)])
    puzzle.add_arrow([(5, 2)], [(6, 1), (7, 0), (8, 0)])
    puzzle.add_arrow([(4, 1)], [(5, 0), (4, 0)])
    puzzle.add_arrow([(1, 4)], [(0, 3), (0, 2)])
    puzzle.add_arrow([(0, 6)], [(0, 7), (1, 8)])
    puzzle.add_arrow([(4, 5)], [(4, 4), (3, 5)])
    puzzle.add_arrow([(2, 4)], [(3, 4), (3, 3)])
    puzzle.add_arrow([(6, 3)], [(5, 4), (5, 3)])
    puzzle.add_arrow([(3, 8)], [(2, 8), (1, 7)])

    return puzzle
