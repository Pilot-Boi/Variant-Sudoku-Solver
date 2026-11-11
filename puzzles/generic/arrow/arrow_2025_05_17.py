"""PuzzleMadness Arrow Sudoku — 2025-05-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-05-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/5/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 3)], [(4, 3), (3, 3), (2, 4), (1, 5), (0, 6)])
    puzzle.add_arrow([(7, 3)], [(8, 2), (7, 2), (6, 3)])
    puzzle.add_arrow([(3, 7)], [(3, 6), (4, 7)])
    puzzle.add_arrow([(1, 0)], [(2, 1), (1, 1), (1, 2)])
    puzzle.add_arrow([(6, 6)], [(6, 5), (7, 5)])
    puzzle.add_arrow([(3, 1)], [(3, 0), (2, 0)])
    puzzle.add_arrow([(1, 6)], [(2, 6), (3, 5)])
    puzzle.add_arrow([(6, 8)], [(5, 7), (5, 6)])
    puzzle.add_arrow([(4, 2)], [(5, 1), (5, 0), (4, 0)])
    puzzle.add_arrow([(8, 5)], [(7, 6), (8, 7), (8, 8)])
    puzzle.add_arrow([(2, 7)], [(3, 8), (4, 8)])
    puzzle.add_arrow([(4, 5)], [(5, 5), (6, 4)])
    puzzle.add_arrow([(8, 1)], [(7, 1), (6, 1)])
    puzzle.add_arrow([(2, 2)], [(2, 3), (1, 4)])
    puzzle.add_arrow([(1, 8)], [(0, 7), (0, 8)])
    puzzle.add_arrow([(0, 4)], [(1, 3), (0, 2)])

    return puzzle
