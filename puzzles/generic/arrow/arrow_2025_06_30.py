"""PuzzleMadness Arrow Sudoku — 2025-06-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-06-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/6/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 4, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 9, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 2)], [(2, 2), (3, 3), (2, 3)])
    puzzle.add_arrow([(1, 0)], [(1, 1), (0, 2)])
    puzzle.add_arrow([(2, 6)], [(2, 7), (1, 8)])
    puzzle.add_arrow([(1, 3)], [(1, 4), (2, 5), (3, 5), (4, 5)])
    puzzle.add_arrow([(6, 6)], [(7, 7), (8, 8)])
    puzzle.add_arrow([(8, 1)], [(7, 0), (6, 0), (5, 1), (6, 2)])
    puzzle.add_arrow([(7, 8)], [(8, 7), (8, 6), (7, 6)])
    puzzle.add_arrow([(6, 5)], [(5, 4), (6, 4), (7, 3)])
    puzzle.add_arrow([(2, 0)], [(3, 0), (4, 0)])
    puzzle.add_arrow([(1, 6)], [(0, 5), (0, 6)])
    puzzle.add_arrow([(3, 8)], [(4, 8), (5, 8)])
    puzzle.add_arrow([(5, 6)], [(4, 7), (5, 7)])
    puzzle.add_arrow([(4, 2)], [(5, 2), (6, 3)])
    puzzle.add_arrow([(8, 0)], [(7, 1), (8, 2)])
    puzzle.add_arrow([(7, 4)], [(8, 3), (7, 2)])
    puzzle.add_arrow([(1, 7)], [(2, 8), (3, 7)])

    return puzzle
