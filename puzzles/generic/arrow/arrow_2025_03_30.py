"""PuzzleMadness Arrow Sudoku — 2025-03-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-03-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/3/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 9, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 3)], [(4, 4), (5, 4)])
    puzzle.add_arrow([(3, 4)], [(2, 4), (3, 3)])
    puzzle.add_arrow([(6, 6)], [(7, 6), (6, 7)])
    puzzle.add_arrow([(0, 1)], [(1, 2), (0, 2)])
    puzzle.add_arrow([(5, 7)], [(4, 7), (5, 8), (6, 8)])
    puzzle.add_arrow([(1, 6)], [(0, 5), (1, 5), (2, 6)])
    puzzle.add_arrow([(7, 3)], [(7, 4), (6, 5), (5, 5), (5, 6)])
    puzzle.add_arrow([(3, 8)], [(3, 7), (3, 6)])
    puzzle.add_arrow([(2, 2)], [(1, 1), (0, 0), (1, 0)])
    puzzle.add_arrow([(5, 0)], [(4, 1), (5, 2)])
    puzzle.add_arrow([(3, 2)], [(3, 1), (3, 0), (4, 0)])
    puzzle.add_arrow([(1, 7)], [(0, 8), (1, 8)])
    puzzle.add_arrow([(7, 7)], [(8, 7), (8, 8)])
    puzzle.add_arrow([(7, 1)], [(8, 1), (7, 2)])
    puzzle.add_arrow([(2, 5)], [(1, 4), (2, 3)])
    puzzle.add_arrow([(6, 1)], [(6, 2), (5, 3)])
    puzzle.add_arrow([(8, 4)], [(8, 5), (7, 5)])

    return puzzle
