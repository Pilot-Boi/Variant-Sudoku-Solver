"""PuzzleMadness Arrow Sudoku — 2025-06-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-06-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/6/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 8, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 5)], [(2, 6), (1, 6), (0, 6)])
    puzzle.add_arrow([(1, 0)], [(1, 1), (2, 2)])
    puzzle.add_arrow([(5, 4)], [(4, 4), (4, 3)])
    puzzle.add_arrow([(8, 6)], [(7, 6), (7, 7), (7, 8)])
    puzzle.add_arrow([(7, 1)], [(8, 1), (8, 0)])
    puzzle.add_arrow([(0, 2)], [(1, 2), (2, 3), (3, 3)])
    puzzle.add_arrow([(2, 8)], [(1, 7), (0, 7)])
    puzzle.add_arrow([(7, 4)], [(7, 5), (6, 6), (5, 6)])
    puzzle.add_arrow([(5, 7)], [(6, 7), (6, 8)])
    puzzle.add_arrow([(5, 1)], [(4, 0), (3, 1)])
    puzzle.add_arrow([(6, 3)], [(6, 4), (5, 3)])
    puzzle.add_arrow([(3, 6)], [(3, 7), (4, 7)])
    puzzle.add_arrow([(2, 4)], [(2, 5), (1, 4)])
    puzzle.add_arrow([(7, 2)], [(8, 3), (8, 4)])
    puzzle.add_arrow([(6, 2)], [(7, 3), (8, 2)])
    puzzle.add_arrow([(3, 0)], [(2, 1), (3, 2)])
    puzzle.add_arrow([(1, 3)], [(0, 4), (1, 5)])

    return puzzle
