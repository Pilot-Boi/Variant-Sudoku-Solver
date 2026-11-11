"""PuzzleMadness Arrow Sudoku — 2025-10-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 5, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 7)], [(6, 6), (7, 5), (8, 6), (8, 5)])
    puzzle.add_arrow([(1, 7)], [(2, 8), (2, 7), (1, 8)])
    puzzle.add_arrow([(5, 1)], [(4, 2), (4, 3), (5, 2), (4, 1)])
    puzzle.add_arrow([(6, 3)], [(6, 4), (5, 3)])
    puzzle.add_arrow([(1, 3)], [(1, 4), (0, 4), (0, 3)])
    puzzle.add_arrow([(4, 5)], [(4, 6), (3, 6)])
    puzzle.add_arrow([(6, 5)], [(5, 4), (5, 5), (5, 6)])
    puzzle.add_arrow([(7, 2)], [(6, 1), (7, 1), (6, 0)])
    puzzle.add_arrow([(3, 5)], [(2, 5), (2, 4)])
    puzzle.add_arrow([(7, 6)], [(8, 7), (7, 8)])
    puzzle.add_arrow([(8, 2)], [(8, 3), (7, 3)])
    puzzle.add_arrow([(2, 1)], [(1, 2), (0, 1), (1, 0)])
    puzzle.add_arrow([(0, 2)], [(1, 1), (0, 0)])
    puzzle.add_arrow([(2, 6)], [(1, 6), (0, 7)])
    puzzle.add_arrow([(3, 4)], [(3, 3), (3, 2)])

    return puzzle
