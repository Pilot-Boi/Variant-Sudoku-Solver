"""PuzzleMadness Arrow Sudoku — 2025-05-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-05-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/5/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 7, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 5)], [(3, 4), (2, 5), (3, 6)])
    puzzle.add_arrow([(2, 7)], [(1, 6), (2, 6)])
    puzzle.add_arrow([(6, 1)], [(5, 1), (6, 0), (7, 0), (7, 1)])
    puzzle.add_arrow([(7, 5)], [(8, 4), (7, 4), (6, 3)])
    puzzle.add_arrow([(2, 0)], [(2, 1), (1, 2), (0, 2)])
    puzzle.add_arrow([(0, 6)], [(0, 7), (1, 7)])
    puzzle.add_arrow([(7, 7)], [(6, 8), (5, 7)])
    puzzle.add_arrow([(3, 3)], [(4, 3), (4, 4), (5, 5)])
    puzzle.add_arrow([(4, 2)], [(5, 2), (6, 2)])
    puzzle.add_arrow([(3, 2)], [(4, 1), (5, 0)])
    puzzle.add_arrow([(8, 2)], [(8, 1), (8, 0)])
    puzzle.add_arrow([(4, 7)], [(3, 8), (4, 8), (3, 7)])
    puzzle.add_arrow([(1, 3)], [(0, 4), (1, 5)])
    puzzle.add_arrow([(0, 0)], [(1, 1), (2, 2)])
    puzzle.add_arrow([(6, 7)], [(7, 6), (6, 5)])
    puzzle.add_arrow([(2, 3)], [(1, 4), (0, 3)])

    return puzzle
