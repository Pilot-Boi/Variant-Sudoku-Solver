"""PuzzleMadness Arrow Sudoku — 2025-09-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 1)], [(6, 2), (7, 2), (8, 3), (7, 3)])
    puzzle.add_arrow([(0, 5)], [(1, 5), (2, 4), (3, 5), (2, 5)])
    puzzle.add_arrow([(7, 5)], [(7, 6), (8, 5)])
    puzzle.add_arrow([(4, 6)], [(3, 6), (2, 7), (1, 7)])
    puzzle.add_arrow([(1, 2)], [(0, 1), (1, 0)])
    puzzle.add_arrow([(4, 0)], [(4, 1), (5, 1)])
    puzzle.add_arrow([(6, 3)], [(5, 3), (4, 2)])
    puzzle.add_arrow([(5, 4)], [(6, 5), (7, 4)])
    puzzle.add_arrow([(0, 3)], [(0, 4), (1, 3)])
    puzzle.add_arrow([(7, 7)], [(6, 6), (5, 6), (5, 5)])
    puzzle.add_arrow([(3, 0)], [(3, 1), (2, 0)])
    puzzle.add_arrow([(7, 0)], [(6, 0), (5, 0)])
    puzzle.add_arrow([(3, 4)], [(3, 3), (4, 4)])
    puzzle.add_arrow([(2, 3)], [(3, 2), (4, 3)])
    puzzle.add_arrow([(5, 8)], [(4, 7), (3, 7)])
    puzzle.add_arrow([(0, 7)], [(1, 8), (2, 8)])
    puzzle.add_arrow([(8, 2)], [(8, 1), (8, 0)])
    puzzle.add_arrow([(2, 2)], [(1, 1), (0, 0)])

    return puzzle
