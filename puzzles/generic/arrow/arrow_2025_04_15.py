"""PuzzleMadness Arrow Sudoku — 2025-04-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 5)], [(4, 5), (3, 5), (3, 4)])
    puzzle.add_arrow([(2, 0)], [(1, 1), (0, 1)])
    puzzle.add_arrow([(7, 6)], [(8, 7), (7, 8), (8, 8)])
    puzzle.add_arrow([(8, 0)], [(7, 1), (6, 2)])
    puzzle.add_arrow([(3, 0)], [(4, 1), (5, 0)])
    puzzle.add_arrow([(4, 2)], [(5, 2), (6, 3)])
    puzzle.add_arrow([(0, 3)], [(0, 2), (1, 3), (0, 4)])
    puzzle.add_arrow([(8, 2)], [(8, 3), (7, 3), (7, 2)])
    puzzle.add_arrow([(4, 8)], [(4, 7), (5, 7), (4, 6)])
    puzzle.add_arrow([(2, 5)], [(1, 6), (2, 7)])
    puzzle.add_arrow([(3, 6)], [(3, 7), (2, 6)])
    puzzle.add_arrow([(0, 7)], [(0, 6), (0, 5)])
    puzzle.add_arrow([(5, 8)], [(6, 7), (7, 7)])
    puzzle.add_arrow([(2, 1)], [(2, 2), (3, 3)])
    puzzle.add_arrow([(6, 1)], [(5, 1), (4, 0)])
    puzzle.add_arrow([(6, 4)], [(5, 4), (6, 5)])
    puzzle.add_arrow([(0, 8)], [(1, 8), (2, 8)])
    puzzle.add_arrow([(7, 5)], [(7, 4), (8, 5)])

    return puzzle
