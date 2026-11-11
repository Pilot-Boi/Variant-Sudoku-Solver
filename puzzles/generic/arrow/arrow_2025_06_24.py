"""PuzzleMadness Arrow Sudoku — 2025-06-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-06-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/6/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 5],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 0)], [(4, 1), (3, 2)])
    puzzle.add_arrow([(4, 5)], [(3, 4), (2, 5), (2, 6)])
    puzzle.add_arrow([(7, 4)], [(6, 4), (5, 4)])
    puzzle.add_arrow([(6, 2)], [(7, 3), (8, 4)])
    puzzle.add_arrow([(0, 6)], [(1, 7), (1, 6)])
    puzzle.add_arrow([(3, 0)], [(2, 1), (2, 0), (1, 1)])
    puzzle.add_arrow([(6, 1)], [(5, 0), (6, 0), (7, 1)])
    puzzle.add_arrow([(2, 3)], [(3, 3), (4, 2)])
    puzzle.add_arrow([(6, 7)], [(6, 6), (5, 6)])
    puzzle.add_arrow([(0, 4)], [(0, 3), (1, 3), (0, 2)])
    puzzle.add_arrow([(8, 8)], [(8, 7), (8, 6), (8, 5)])
    puzzle.add_arrow([(2, 4)], [(1, 5), (1, 4)])
    puzzle.add_arrow([(4, 8)], [(4, 7), (3, 8)])
    puzzle.add_arrow([(4, 6)], [(5, 7), (6, 8)])
    puzzle.add_arrow([(2, 7)], [(1, 8), (0, 8), (0, 7)])
    puzzle.add_arrow([(8, 2)], [(8, 1), (7, 0)])
    puzzle.add_arrow([(5, 5)], [(4, 4), (5, 3)])

    return puzzle
