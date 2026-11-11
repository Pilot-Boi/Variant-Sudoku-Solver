"""PuzzleMadness Arrow Sudoku — 2025-04-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 6, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 7)], [(5, 6), (5, 5), (4, 5)])
    puzzle.add_arrow([(6, 7)], [(7, 7), (8, 6)])
    puzzle.add_arrow([(4, 1)], [(3, 1), (2, 2), (1, 3), (2, 4)])
    puzzle.add_arrow([(7, 3)], [(8, 2), (7, 1), (6, 1)])
    puzzle.add_arrow([(6, 6)], [(6, 5), (7, 6)])
    puzzle.add_arrow([(7, 5)], [(7, 4), (8, 3)])
    puzzle.add_arrow([(2, 6)], [(1, 7), (2, 8)])
    puzzle.add_arrow([(3, 5)], [(3, 4), (4, 3), (4, 4)])
    puzzle.add_arrow([(6, 8)], [(5, 7), (4, 8)])
    puzzle.add_arrow([(0, 4)], [(1, 5), (1, 4)])
    puzzle.add_arrow([(5, 1)], [(4, 0), (5, 0)])
    puzzle.add_arrow([(5, 4)], [(6, 3), (5, 2)])
    puzzle.add_arrow([(0, 7)], [(1, 6), (0, 5)])
    puzzle.add_arrow([(1, 2)], [(1, 1), (0, 0)])
    puzzle.add_arrow([(1, 0)], [(2, 1), (2, 0)])
    puzzle.add_arrow([(0, 3)], [(0, 2), (0, 1)])

    return puzzle
