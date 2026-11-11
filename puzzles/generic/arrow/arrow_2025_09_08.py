"""PuzzleMadness Arrow Sudoku — 2025-09-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 1, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 2)], [(3, 2), (2, 2)])
    puzzle.add_arrow([(3, 6)], [(3, 7), (2, 6), (1, 6)])
    puzzle.add_arrow([(6, 5)], [(5, 6), (5, 7)])
    puzzle.add_arrow([(8, 3)], [(7, 4), (6, 3)])
    puzzle.add_arrow([(0, 1)], [(0, 2), (1, 2), (2, 1)])
    puzzle.add_arrow([(2, 3)], [(3, 4), (3, 5)])
    puzzle.add_arrow([(6, 8)], [(7, 7), (8, 7)])
    puzzle.add_arrow([(6, 1)], [(5, 0), (5, 1)])
    puzzle.add_arrow([(5, 3)], [(5, 4), (4, 5)])
    puzzle.add_arrow([(2, 8)], [(1, 7), (0, 6)])
    puzzle.add_arrow([(0, 3)], [(0, 4), (0, 5)])
    puzzle.add_arrow([(3, 3)], [(4, 3), (4, 4)])
    puzzle.add_arrow([(7, 1)], [(7, 2), (6, 2)])
    puzzle.add_arrow([(7, 6)], [(6, 7), (7, 8)])
    puzzle.add_arrow([(6, 6)], [(7, 5), (6, 4)])
    puzzle.add_arrow([(2, 0)], [(3, 1), (4, 1), (4, 0)])
    puzzle.add_arrow([(7, 3)], [(8, 2), (8, 1)])
    puzzle.add_arrow([(4, 7)], [(3, 8), (2, 7)])

    return puzzle
