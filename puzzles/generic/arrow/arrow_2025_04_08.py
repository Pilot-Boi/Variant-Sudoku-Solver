"""PuzzleMadness Arrow Sudoku — 2025-04-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 5, 0, 0, 7, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 3, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 8)], [(6, 7), (6, 8), (7, 8)])
    puzzle.add_arrow([(1, 4)], [(0, 5), (1, 6), (2, 5)])
    puzzle.add_arrow([(5, 2)], [(6, 1), (7, 2)])
    puzzle.add_arrow([(0, 7)], [(1, 7), (0, 8)])
    puzzle.add_arrow([(7, 4)], [(7, 5), (6, 5), (5, 4)])
    puzzle.add_arrow([(4, 1)], [(3, 1), (3, 2)])
    puzzle.add_arrow([(5, 5)], [(4, 4), (4, 5), (3, 6)])
    puzzle.add_arrow([(2, 7)], [(3, 7), (4, 7), (5, 7)])
    puzzle.add_arrow([(6, 6)], [(7, 7), (8, 8)])
    puzzle.add_arrow([(8, 3)], [(8, 4), (7, 3)])
    puzzle.add_arrow([(0, 0)], [(1, 1), (2, 1)])
    puzzle.add_arrow([(1, 3)], [(2, 3), (1, 2), (0, 2)])
    puzzle.add_arrow([(5, 1)], [(6, 0), (5, 0)])
    puzzle.add_arrow([(6, 4)], [(5, 3), (4, 3)])
    puzzle.add_arrow([(8, 1)], [(8, 2), (7, 1)])
    puzzle.add_arrow([(3, 5)], [(3, 4), (2, 4)])

    return puzzle
