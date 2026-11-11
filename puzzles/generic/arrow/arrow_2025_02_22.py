"""PuzzleMadness Arrow Sudoku — 2025-02-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 0, 0, 0, 8],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 5, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 0)], [(1, 0), (2, 1)])
    puzzle.add_arrow([(4, 7)], [(5, 8), (5, 7)])
    puzzle.add_arrow([(5, 5)], [(4, 6), (4, 5)])
    puzzle.add_arrow([(6, 2)], [(5, 2), (6, 1), (7, 2)])
    puzzle.add_arrow([(0, 1)], [(1, 1), (0, 2), (1, 3)])
    puzzle.add_arrow([(8, 7)], [(8, 6), (7, 6), (6, 7)])
    puzzle.add_arrow([(3, 5)], [(3, 4), (4, 3)])
    puzzle.add_arrow([(6, 4)], [(7, 4), (7, 3), (8, 4)])
    puzzle.add_arrow([(0, 6)], [(0, 5), (1, 5)])
    puzzle.add_arrow([(1, 7)], [(2, 7), (1, 6), (2, 5)])
    puzzle.add_arrow([(4, 2)], [(3, 1), (3, 0), (4, 1)])
    puzzle.add_arrow([(6, 0)], [(7, 1), (8, 2)])
    puzzle.add_arrow([(3, 8)], [(2, 8), (3, 7)])
    puzzle.add_arrow([(7, 8)], [(7, 7), (6, 6)])

    return puzzle
