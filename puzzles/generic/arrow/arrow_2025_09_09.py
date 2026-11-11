"""PuzzleMadness Arrow Sudoku — 2025-09-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(8, 6)], [(8, 7), (7, 6)])
    puzzle.add_arrow([(2, 5)], [(2, 4), (3, 3), (4, 2), (4, 3)])
    puzzle.add_arrow([(2, 8)], [(3, 7), (2, 6)])
    puzzle.add_arrow([(5, 4)], [(6, 5), (6, 6)])
    puzzle.add_arrow([(1, 1)], [(1, 0), (2, 0)])
    puzzle.add_arrow([(7, 3)], [(7, 2), (6, 3)])
    puzzle.add_arrow([(5, 1)], [(6, 1), (5, 2), (4, 1)])
    puzzle.add_arrow([(1, 5)], [(1, 6), (0, 5), (1, 4)])
    puzzle.add_arrow([(6, 0)], [(7, 0), (8, 0)])
    puzzle.add_arrow([(6, 8)], [(5, 7), (4, 8)])
    puzzle.add_arrow([(8, 1)], [(7, 1), (6, 2)])
    puzzle.add_arrow([(3, 1)], [(2, 1), (3, 0)])
    puzzle.add_arrow([(3, 4)], [(4, 4), (5, 5)])
    puzzle.add_arrow([(4, 7)], [(3, 6), (2, 7)])
    puzzle.add_arrow([(1, 2)], [(2, 2), (1, 3), (0, 4)])
    puzzle.add_arrow([(8, 4)], [(7, 5), (8, 5)])
    puzzle.add_arrow([(0, 7)], [(1, 7), (1, 8)])
    puzzle.add_arrow([(7, 7)], [(6, 7), (7, 8)])

    return puzzle
