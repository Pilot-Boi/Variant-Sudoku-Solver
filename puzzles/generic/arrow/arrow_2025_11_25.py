"""PuzzleMadness Arrow Sudoku — 2025-11-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 7)], [(4, 8), (5, 7), (6, 6)])
    puzzle.add_arrow([(7, 3)], [(7, 2), (6, 3), (5, 2), (4, 2)])
    puzzle.add_arrow([(3, 5)], [(4, 6), (5, 5), (5, 4), (6, 4)])
    puzzle.add_arrow([(7, 1)], [(7, 0), (6, 1)])
    puzzle.add_arrow([(2, 6)], [(1, 7), (1, 6), (1, 5)])
    puzzle.add_arrow([(0, 2)], [(1, 3), (2, 2)])
    puzzle.add_arrow([(4, 1)], [(4, 0), (3, 1), (2, 0)])
    puzzle.add_arrow([(2, 5)], [(3, 4), (2, 3), (1, 4)])
    puzzle.add_arrow([(8, 7)], [(7, 8), (6, 7)])
    puzzle.add_arrow([(8, 4)], [(8, 5), (8, 6)])
    puzzle.add_arrow([(3, 7)], [(3, 6), (2, 7)])
    puzzle.add_arrow([(1, 0)], [(2, 1), (1, 2)])
    puzzle.add_arrow([(6, 8)], [(7, 7), (8, 8)])
    puzzle.add_arrow([(7, 4)], [(8, 3), (8, 2)])
    puzzle.add_arrow([(6, 2)], [(5, 3), (4, 3)])

    return puzzle
