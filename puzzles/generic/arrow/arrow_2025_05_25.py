"""PuzzleMadness Arrow Sudoku — 2025-05-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-05-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/5/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 7)], [(2, 6), (2, 7), (3, 6)])
    puzzle.add_arrow([(7, 6)], [(6, 6), (5, 6)])
    puzzle.add_arrow([(6, 5)], [(6, 4), (5, 5), (4, 5), (4, 4)])
    puzzle.add_arrow([(5, 3)], [(4, 2), (3, 2)])
    puzzle.add_arrow([(1, 2)], [(1, 3), (2, 4)])
    puzzle.add_arrow([(5, 7)], [(5, 8), (6, 7), (7, 8)])
    puzzle.add_arrow([(8, 1)], [(8, 2), (7, 3)])
    puzzle.add_arrow([(0, 2)], [(0, 1), (0, 0), (1, 0)])
    puzzle.add_arrow([(4, 1)], [(3, 1), (2, 2)])
    puzzle.add_arrow([(2, 1)], [(2, 0), (1, 1)])
    puzzle.add_arrow([(8, 4)], [(8, 3), (7, 4)])
    puzzle.add_arrow([(5, 2)], [(6, 2), (7, 2)])
    puzzle.add_arrow([(6, 0)], [(6, 1), (7, 0)])
    puzzle.add_arrow([(2, 5)], [(1, 4), (1, 5)])
    puzzle.add_arrow([(1, 7)], [(0, 6), (0, 5)])
    puzzle.add_arrow([(0, 7)], [(1, 8), (2, 8)])
    puzzle.add_arrow([(4, 3)], [(3, 4), (2, 3)])
    puzzle.add_arrow([(3, 0)], [(4, 0), (5, 0)])
    puzzle.add_arrow([(8, 8)], [(8, 7), (8, 6)])

    return puzzle
