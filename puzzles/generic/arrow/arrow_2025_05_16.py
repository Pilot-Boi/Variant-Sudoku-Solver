"""PuzzleMadness Arrow Sudoku — 2025-05-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-05-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/5/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 8, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 4)], [(2, 5), (3, 4), (4, 5)])
    puzzle.add_arrow([(6, 5)], [(5, 6), (5, 7), (4, 6)])
    puzzle.add_arrow([(2, 3)], [(3, 3), (2, 2), (1, 3)])
    puzzle.add_arrow([(7, 5)], [(8, 5), (7, 6), (8, 7)])
    puzzle.add_arrow([(6, 1)], [(7, 1), (8, 1), (7, 2)])
    puzzle.add_arrow([(2, 6)], [(1, 7), (0, 8)])
    puzzle.add_arrow([(8, 4)], [(7, 4), (6, 3)])
    puzzle.add_arrow([(5, 8)], [(4, 7), (3, 7)])
    puzzle.add_arrow([(0, 7)], [(1, 6), (1, 5)])
    puzzle.add_arrow([(8, 0)], [(7, 0), (6, 0)])
    puzzle.add_arrow([(5, 4)], [(4, 3), (4, 4)])
    puzzle.add_arrow([(4, 1)], [(3, 1), (2, 1)])
    puzzle.add_arrow([(0, 3)], [(1, 2), (0, 1)])
    puzzle.add_arrow([(3, 6)], [(3, 5), (2, 4)])
    puzzle.add_arrow([(8, 6)], [(7, 7), (7, 8)])
    puzzle.add_arrow([(6, 7)], [(6, 6), (5, 5)])
    puzzle.add_arrow([(5, 1)], [(4, 0), (3, 0)])

    return puzzle
