"""PuzzleMadness Arrow Sudoku — 2025-10-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 6)], [(5, 7), (4, 6), (3, 5), (2, 6)])
    puzzle.add_arrow([(3, 4)], [(3, 3), (2, 3)])
    puzzle.add_arrow([(4, 1)], [(5, 0), (5, 1), (6, 1)])
    puzzle.add_arrow([(2, 0)], [(1, 1), (0, 2), (1, 3), (1, 2)])
    puzzle.add_arrow([(3, 7)], [(3, 8), (4, 7)])
    puzzle.add_arrow([(7, 5)], [(6, 4), (7, 3)])
    puzzle.add_arrow([(8, 5)], [(8, 4), (8, 3)])
    puzzle.add_arrow([(4, 3)], [(4, 2), (5, 3), (6, 3)])
    puzzle.add_arrow([(8, 8)], [(7, 7), (8, 7)])
    puzzle.add_arrow([(1, 5)], [(0, 6), (1, 7)])
    puzzle.add_arrow([(8, 0)], [(7, 1), (8, 1), (7, 0)])
    puzzle.add_arrow([(5, 4)], [(6, 5), (5, 5), (4, 5)])
    puzzle.add_arrow([(3, 1)], [(2, 1), (3, 0)])
    puzzle.add_arrow([(0, 7)], [(1, 8), (0, 8)])
    puzzle.add_arrow([(1, 4)], [(0, 4), (0, 5)])

    return puzzle
