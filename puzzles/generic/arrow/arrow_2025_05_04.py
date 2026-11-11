"""PuzzleMadness Arrow Sudoku — 2025-05-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-05-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/5/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 9, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 2)], [(3, 3), (2, 4)])
    puzzle.add_arrow([(3, 8)], [(2, 7), (1, 8), (1, 7)])
    puzzle.add_arrow([(7, 1)], [(7, 2), (8, 1)])
    puzzle.add_arrow([(5, 3)], [(4, 4), (5, 5), (5, 6), (4, 6)])
    puzzle.add_arrow([(0, 6)], [(1, 5), (1, 6)])
    puzzle.add_arrow([(6, 4)], [(7, 5), (7, 6)])
    puzzle.add_arrow([(5, 4)], [(6, 3), (7, 3), (6, 2)])
    puzzle.add_arrow([(2, 3)], [(3, 4), (4, 3)])
    puzzle.add_arrow([(4, 0)], [(3, 0), (3, 1), (2, 0)])
    puzzle.add_arrow([(1, 1)], [(0, 0), (0, 1), (1, 2)])
    puzzle.add_arrow([(6, 7)], [(7, 8), (8, 7)])
    puzzle.add_arrow([(5, 7)], [(4, 8), (4, 7)])
    puzzle.add_arrow([(0, 3)], [(0, 4), (1, 4)])
    puzzle.add_arrow([(5, 1)], [(6, 1), (6, 0)])
    puzzle.add_arrow([(4, 1)], [(3, 2), (2, 2)])
    puzzle.add_arrow([(8, 5)], [(8, 4), (8, 3)])

    return puzzle
