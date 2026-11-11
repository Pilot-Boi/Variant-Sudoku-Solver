"""PuzzleMadness Arrow Sudoku — 2025-11-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 3)], [(4, 4), (5, 5), (6, 4), (7, 3), (6, 2)])
    puzzle.add_arrow([(5, 1)], [(5, 2), (4, 1), (5, 0), (6, 1)])
    puzzle.add_arrow([(1, 2)], [(0, 2), (1, 1), (1, 0)])
    puzzle.add_arrow([(0, 7)], [(1, 6), (2, 7), (3, 8)])
    puzzle.add_arrow([(8, 4)], [(8, 5), (7, 6), (8, 7)])
    puzzle.add_arrow([(1, 3)], [(2, 4), (1, 4)])
    puzzle.add_arrow([(2, 2)], [(3, 2), (2, 3)])
    puzzle.add_arrow([(4, 7)], [(3, 6), (3, 7), (2, 8)])
    puzzle.add_arrow([(8, 2)], [(8, 1), (7, 2)])
    puzzle.add_arrow([(7, 8)], [(7, 7), (8, 6)])
    puzzle.add_arrow([(2, 5)], [(3, 4), (4, 3)])
    puzzle.add_arrow([(7, 5)], [(7, 4), (6, 3)])
    puzzle.add_arrow([(6, 0)], [(7, 0), (8, 0)])
    puzzle.add_arrow([(5, 7)], [(5, 6), (6, 5)])

    return puzzle
