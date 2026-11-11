"""PuzzleMadness Arrow Sudoku — 2025-10-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 4)], [(3, 5), (4, 5), (3, 4)])
    puzzle.add_arrow([(2, 1)], [(1, 2), (1, 1)])
    puzzle.add_arrow([(5, 8)], [(4, 7), (5, 7)])
    puzzle.add_arrow([(7, 6)], [(8, 6), (7, 7)])
    puzzle.add_arrow([(5, 1)], [(4, 1), (3, 0)])
    puzzle.add_arrow([(5, 2)], [(6, 1), (6, 0)])
    puzzle.add_arrow([(6, 4)], [(7, 5), (8, 4)])
    puzzle.add_arrow([(2, 2)], [(1, 3), (0, 3), (0, 2), (0, 1)])
    puzzle.add_arrow([(6, 3)], [(7, 4), (8, 3)])
    puzzle.add_arrow([(1, 7)], [(2, 7), (1, 6)])
    puzzle.add_arrow([(3, 6)], [(3, 7), (4, 6), (5, 6)])
    puzzle.add_arrow([(1, 5)], [(1, 4), (2, 3), (3, 2)])
    puzzle.add_arrow([(7, 0)], [(8, 0), (7, 1)])
    puzzle.add_arrow([(4, 4)], [(5, 3), (4, 3)])
    puzzle.add_arrow([(2, 8)], [(1, 8), (0, 8)])
    puzzle.add_arrow([(6, 6)], [(6, 7), (6, 8)])

    return puzzle
