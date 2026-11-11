"""PuzzleMadness Arrow Sudoku — 2025-04-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 4)], [(2, 5), (1, 5), (0, 6), (0, 7)])
    puzzle.add_arrow([(6, 2)], [(6, 1), (5, 1)])
    puzzle.add_arrow([(3, 3)], [(3, 4), (2, 3), (1, 4)])
    puzzle.add_arrow([(1, 0)], [(0, 1), (1, 2)])
    puzzle.add_arrow([(7, 7)], [(6, 8), (7, 8)])
    puzzle.add_arrow([(6, 3)], [(7, 4), (8, 5)])
    puzzle.add_arrow([(6, 4)], [(7, 3), (8, 4)])
    puzzle.add_arrow([(4, 3)], [(5, 4), (5, 3)])
    puzzle.add_arrow([(6, 6)], [(5, 6), (6, 5)])
    puzzle.add_arrow([(4, 1)], [(5, 0), (6, 0)])
    puzzle.add_arrow([(0, 5)], [(1, 6), (1, 7)])
    puzzle.add_arrow([(4, 7)], [(4, 6), (4, 5)])
    puzzle.add_arrow([(5, 8)], [(5, 7), (4, 8)])
    puzzle.add_arrow([(3, 1)], [(2, 1), (2, 2)])
    puzzle.add_arrow([(8, 1)], [(7, 0), (7, 1)])
    puzzle.add_arrow([(3, 6)], [(3, 5), (4, 4)])
    puzzle.add_arrow([(1, 3)], [(0, 2), (1, 1)])
    puzzle.add_arrow([(8, 6)], [(8, 7), (8, 8)])
    puzzle.add_arrow([(2, 7)], [(3, 7), (3, 8)])

    return puzzle
