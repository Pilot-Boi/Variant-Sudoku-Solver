"""PuzzleMadness Arrow Sudoku — 2025-11-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 6)], [(3, 5), (2, 4), (1, 5), (0, 5)])
    puzzle.add_arrow([(5, 5)], [(4, 6), (3, 7), (2, 6), (2, 7)])
    puzzle.add_arrow([(7, 0)], [(8, 1), (8, 0)])
    puzzle.add_arrow([(6, 1)], [(6, 2), (6, 3), (7, 2), (7, 3)])
    puzzle.add_arrow([(7, 4)], [(7, 5), (8, 6)])
    puzzle.add_arrow([(8, 8)], [(7, 7), (6, 6)])
    puzzle.add_arrow([(4, 1)], [(5, 1), (5, 0)])
    puzzle.add_arrow([(6, 8)], [(5, 8), (4, 7)])
    puzzle.add_arrow([(1, 7)], [(1, 8), (0, 7)])
    puzzle.add_arrow([(1, 3)], [(0, 2), (1, 1), (0, 0)])
    puzzle.add_arrow([(3, 3)], [(4, 3), (4, 4)])
    puzzle.add_arrow([(0, 3)], [(1, 4), (2, 3)])
    puzzle.add_arrow([(5, 4)], [(5, 3), (5, 2)])
    puzzle.add_arrow([(4, 0)], [(3, 1), (2, 2)])
    puzzle.add_arrow([(8, 7)], [(7, 6), (8, 5)])
    puzzle.add_arrow([(1, 2)], [(0, 1), (1, 0)])

    return puzzle
