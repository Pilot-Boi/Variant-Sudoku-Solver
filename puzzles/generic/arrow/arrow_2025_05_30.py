"""PuzzleMadness Arrow Sudoku — 2025-05-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-05-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/5/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 2, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 6)], [(1, 7), (2, 7), (3, 6), (2, 5), (2, 4)])
    puzzle.add_arrow([(6, 5)], [(6, 6), (5, 5)])
    puzzle.add_arrow([(3, 2)], [(4, 1), (5, 2), (4, 3), (3, 3)])
    puzzle.add_arrow([(3, 1)], [(4, 0), (5, 0), (6, 0)])
    puzzle.add_arrow([(0, 5)], [(0, 6), (0, 7)])
    puzzle.add_arrow([(8, 3)], [(8, 4), (7, 5), (8, 6)])
    puzzle.add_arrow([(6, 3)], [(6, 2), (7, 1)])
    puzzle.add_arrow([(3, 8)], [(4, 8), (4, 7)])
    puzzle.add_arrow([(7, 7)], [(6, 8), (6, 7)])
    puzzle.add_arrow([(0, 0)], [(1, 1), (1, 0), (0, 1)])
    puzzle.add_arrow([(0, 2)], [(1, 2), (2, 2)])
    puzzle.add_arrow([(6, 4)], [(7, 4), (8, 5)])
    puzzle.add_arrow([(1, 3)], [(0, 4), (1, 5)])
    puzzle.add_arrow([(4, 5)], [(3, 5), (4, 4)])
    puzzle.add_arrow([(7, 2)], [(7, 3), (8, 2)])
    puzzle.add_arrow([(4, 6)], [(3, 7), (2, 8)])

    return puzzle
