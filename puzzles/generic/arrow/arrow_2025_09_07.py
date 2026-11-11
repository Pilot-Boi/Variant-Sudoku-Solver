"""PuzzleMadness Arrow Sudoku — 2025-09-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 6, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 5)], [(4, 4), (3, 4), (2, 5), (3, 6)])
    puzzle.add_arrow([(7, 2)], [(7, 3), (6, 3), (5, 3)])
    puzzle.add_arrow([(6, 6)], [(6, 5), (7, 4)])
    puzzle.add_arrow([(4, 2)], [(5, 2), (5, 1), (5, 0)])
    puzzle.add_arrow([(2, 1)], [(3, 1), (4, 1)])
    puzzle.add_arrow([(3, 3)], [(2, 3), (1, 3)])
    puzzle.add_arrow([(1, 1)], [(2, 0), (1, 0)])
    puzzle.add_arrow([(6, 7)], [(7, 7), (8, 6)])
    puzzle.add_arrow([(1, 7)], [(0, 6), (1, 6)])
    puzzle.add_arrow([(5, 8)], [(4, 8), (4, 7), (4, 6)])
    puzzle.add_arrow([(7, 0)], [(8, 0), (7, 1)])
    puzzle.add_arrow([(0, 4)], [(1, 5), (0, 5)])
    puzzle.add_arrow([(3, 7)], [(3, 8), (2, 7)])
    puzzle.add_arrow([(8, 3)], [(8, 2), (8, 1)])
    puzzle.add_arrow([(4, 3)], [(5, 4), (4, 5)])
    puzzle.add_arrow([(8, 8)], [(8, 7), (7, 6)])

    return puzzle
