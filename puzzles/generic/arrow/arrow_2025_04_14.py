"""PuzzleMadness Arrow Sudoku — 2025-04-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 3, 5, 0, 1],
        [0, 4, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 0)], [(6, 1), (5, 1)])
    puzzle.add_arrow([(1, 1)], [(1, 2), (0, 2)])
    puzzle.add_arrow([(6, 8)], [(7, 7), (6, 7)])
    puzzle.add_arrow([(7, 2)], [(8, 1), (8, 2)])
    puzzle.add_arrow([(2, 8)], [(1, 8), (1, 7), (0, 6)])
    puzzle.add_arrow([(1, 3)], [(2, 2), (3, 1), (4, 1)])
    puzzle.add_arrow([(8, 5)], [(7, 5), (6, 5), (7, 4)])
    puzzle.add_arrow([(5, 3)], [(4, 3), (3, 2)])
    puzzle.add_arrow([(3, 4)], [(2, 3), (3, 3)])
    puzzle.add_arrow([(3, 5)], [(2, 6), (1, 5), (0, 5)])
    puzzle.add_arrow([(6, 4)], [(5, 5), (4, 5)])
    puzzle.add_arrow([(2, 1)], [(2, 0), (1, 0)])
    puzzle.add_arrow([(8, 4)], [(7, 3), (6, 3)])
    puzzle.add_arrow([(4, 7)], [(5, 7), (4, 8)])
    puzzle.add_arrow([(6, 0)], [(7, 1), (8, 0)])
    puzzle.add_arrow([(2, 5)], [(1, 4), (0, 4)])
    puzzle.add_arrow([(7, 6)], [(8, 7), (7, 8)])

    return puzzle
