"""PuzzleMadness Arrow Sudoku — 2025-03-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-03-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/3/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 4)], [(2, 3), (1, 4), (1, 5), (1, 6)])
    puzzle.add_arrow([(4, 0)], [(5, 1), (4, 1), (3, 1)])
    puzzle.add_arrow([(5, 6)], [(6, 5), (5, 5)])
    puzzle.add_arrow([(3, 3)], [(4, 4), (5, 4), (4, 3)])
    puzzle.add_arrow([(1, 1)], [(2, 1), (3, 0)])
    puzzle.add_arrow([(8, 3)], [(8, 2), (7, 2), (6, 2)])
    puzzle.add_arrow([(6, 8)], [(5, 8), (6, 7), (7, 7)])
    puzzle.add_arrow([(6, 4)], [(7, 4), (8, 5)])
    puzzle.add_arrow([(7, 6)], [(8, 7), (7, 8)])
    puzzle.add_arrow([(5, 7)], [(4, 8), (4, 7)])
    puzzle.add_arrow([(2, 5)], [(3, 6), (4, 5)])
    puzzle.add_arrow([(7, 0)], [(6, 0), (7, 1)])
    puzzle.add_arrow([(3, 5)], [(2, 6), (3, 7)])
    puzzle.add_arrow([(1, 8)], [(0, 8), (1, 7), (0, 6)])
    puzzle.add_arrow([(1, 3)], [(0, 3), (0, 2)])
    puzzle.add_arrow([(0, 1)], [(0, 0), (1, 0), (2, 0)])

    return puzzle
