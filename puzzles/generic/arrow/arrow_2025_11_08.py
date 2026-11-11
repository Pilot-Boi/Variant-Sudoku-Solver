"""PuzzleMadness Arrow Sudoku — 2025-11-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 3, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(0, 3)], [(0, 4), (1, 3), (0, 2)])
    puzzle.add_arrow([(4, 6)], [(3, 6), (2, 6)])
    puzzle.add_arrow([(7, 6)], [(6, 6), (7, 5)])
    puzzle.add_arrow([(3, 4)], [(4, 5), (3, 5)])
    puzzle.add_arrow([(7, 0)], [(6, 1), (7, 1), (6, 0)])
    puzzle.add_arrow([(2, 1)], [(1, 1), (2, 0)])
    puzzle.add_arrow([(1, 7)], [(2, 8), (3, 7), (2, 7), (1, 8)])
    puzzle.add_arrow([(4, 7)], [(4, 8), (3, 8)])
    puzzle.add_arrow([(0, 1)], [(1, 0), (0, 0)])
    puzzle.add_arrow([(6, 3)], [(7, 4), (8, 5)])
    puzzle.add_arrow([(7, 8)], [(8, 7), (8, 6)])
    puzzle.add_arrow([(2, 4)], [(3, 3), (2, 2)])
    puzzle.add_arrow([(6, 4)], [(5, 5), (4, 4)])
    puzzle.add_arrow([(4, 3)], [(5, 3), (4, 2), (4, 1)])
    puzzle.add_arrow([(5, 8)], [(5, 7), (6, 7)])
    puzzle.add_arrow([(8, 3)], [(8, 4), (7, 3)])
    puzzle.add_arrow([(5, 1)], [(4, 0), (3, 1)])
    puzzle.add_arrow([(3, 2)], [(2, 3), (1, 2)])
    puzzle.add_arrow([(7, 2)], [(8, 1), (8, 2)])

    return puzzle
