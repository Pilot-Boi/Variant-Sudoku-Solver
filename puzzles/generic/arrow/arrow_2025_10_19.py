"""PuzzleMadness Arrow Sudoku — 2025-10-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 2)], [(6, 1), (7, 1), (8, 1)])
    puzzle.add_arrow([(4, 7)], [(3, 6), (4, 5), (5, 5)])
    puzzle.add_arrow([(2, 8)], [(3, 7), (2, 6), (2, 5), (2, 4)])
    puzzle.add_arrow([(6, 5)], [(6, 4), (5, 4), (5, 3), (4, 2)])
    puzzle.add_arrow([(5, 7)], [(6, 6), (5, 6)])
    puzzle.add_arrow([(8, 7)], [(7, 7), (6, 7)])
    puzzle.add_arrow([(3, 2)], [(4, 1), (4, 0)])
    puzzle.add_arrow([(3, 0)], [(2, 0), (3, 1)])
    puzzle.add_arrow([(7, 6)], [(7, 5), (8, 4)])
    puzzle.add_arrow([(1, 4)], [(1, 3), (1, 2), (2, 2)])
    puzzle.add_arrow([(4, 3)], [(3, 3), (3, 4)])
    puzzle.add_arrow([(2, 7)], [(1, 8), (0, 7), (0, 8)])
    puzzle.add_arrow([(0, 5)], [(1, 6), (1, 5)])
    puzzle.add_arrow([(0, 1)], [(1, 1), (0, 0)])
    puzzle.add_arrow([(6, 3)], [(7, 3), (8, 2)])
    puzzle.add_arrow([(7, 0)], [(6, 0), (5, 0)])

    return puzzle
