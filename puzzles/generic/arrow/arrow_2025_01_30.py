"""PuzzleMadness Arrow Sudoku — 2025-01-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 8, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 1)], [(4, 1), (3, 2), (2, 2), (2, 3), (3, 3)])
    puzzle.add_arrow([(6, 2)], [(7, 2), (7, 1)])
    puzzle.add_arrow([(7, 6)], [(8, 6), (8, 5), (8, 4)])
    puzzle.add_arrow([(3, 0)], [(4, 0), (5, 0), (6, 0)])
    puzzle.add_arrow([(1, 5)], [(1, 6), (2, 5), (1, 4)])
    puzzle.add_arrow([(5, 5)], [(5, 6), (6, 5), (7, 5)])
    puzzle.add_arrow([(6, 7)], [(7, 8), (8, 7)])
    puzzle.add_arrow([(2, 4)], [(3, 4), (3, 5)])
    puzzle.add_arrow([(0, 5)], [(0, 4), (1, 3)])
    puzzle.add_arrow([(0, 8)], [(1, 7), (0, 6)])
    puzzle.add_arrow([(2, 1)], [(1, 1), (0, 2)])
    puzzle.add_arrow([(4, 2)], [(4, 3), (5, 2)])
    puzzle.add_arrow([(6, 8)], [(5, 8), (4, 8)])
    puzzle.add_arrow([(4, 7)], [(3, 6), (4, 6)])

    return puzzle
