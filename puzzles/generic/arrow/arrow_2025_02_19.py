"""PuzzleMadness Arrow Sudoku — 2025-02-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(0, 0)], [(0, 1), (0, 2)])
    puzzle.add_arrow([(4, 5)], [(3, 4), (4, 3)])
    puzzle.add_arrow([(4, 6)], [(5, 6), (6, 5), (6, 4)])
    puzzle.add_arrow([(0, 5)], [(0, 6), (1, 5), (2, 6), (3, 6)])
    puzzle.add_arrow([(0, 3)], [(1, 3), (2, 3), (3, 3)])
    puzzle.add_arrow([(8, 3)], [(8, 2), (7, 2), (6, 1), (5, 1)])
    puzzle.add_arrow([(7, 7)], [(8, 7), (8, 8)])
    puzzle.add_arrow([(1, 2)], [(1, 1), (2, 0)])
    puzzle.add_arrow([(3, 2)], [(4, 1), (4, 2)])
    puzzle.add_arrow([(4, 4)], [(5, 3), (6, 2)])
    puzzle.add_arrow([(2, 7)], [(2, 8), (3, 7)])
    puzzle.add_arrow([(2, 4)], [(2, 5), (1, 4)])
    puzzle.add_arrow([(6, 8)], [(5, 7), (4, 7)])
    puzzle.add_arrow([(6, 6)], [(6, 7), (7, 8)])
    puzzle.add_arrow([(3, 0)], [(4, 0), (5, 0)])
    puzzle.add_arrow([(1, 6)], [(1, 7), (1, 8)])
    puzzle.add_arrow([(8, 4)], [(7, 5), (7, 4)])
    puzzle.add_arrow([(5, 2)], [(6, 3), (5, 4)])

    return puzzle
