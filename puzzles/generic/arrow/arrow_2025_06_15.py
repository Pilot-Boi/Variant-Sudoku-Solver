"""PuzzleMadness Arrow Sudoku — 2025-06-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-06-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/6/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 4)], [(5, 5), (6, 4), (6, 3)])
    puzzle.add_arrow([(6, 7)], [(5, 7), (4, 6), (3, 5)])
    puzzle.add_arrow([(0, 1)], [(1, 2), (2, 1)])
    puzzle.add_arrow([(0, 5)], [(1, 4), (2, 4)])
    puzzle.add_arrow([(7, 2)], [(8, 3), (7, 4)])
    puzzle.add_arrow([(8, 0)], [(7, 1), (8, 2), (8, 1)])
    puzzle.add_arrow([(2, 3)], [(3, 3), (2, 2)])
    puzzle.add_arrow([(5, 8)], [(6, 8), (7, 7), (7, 6)])
    puzzle.add_arrow([(6, 2)], [(6, 1), (5, 0), (6, 0)])
    puzzle.add_arrow([(0, 7)], [(1, 7), (0, 6), (1, 5)])
    puzzle.add_arrow([(8, 4)], [(8, 5), (7, 5)])
    puzzle.add_arrow([(4, 0)], [(5, 1), (4, 2)])
    puzzle.add_arrow([(3, 7)], [(4, 8), (3, 8)])
    puzzle.add_arrow([(3, 4)], [(4, 4), (5, 3)])
    puzzle.add_arrow([(1, 3)], [(0, 3), (0, 4)])
    puzzle.add_arrow([(5, 2)], [(4, 3), (3, 2)])
    puzzle.add_arrow([(2, 6)], [(3, 6), (4, 7)])
    puzzle.add_arrow([(1, 1)], [(1, 0), (2, 0), (3, 0)])

    return puzzle
