"""PuzzleMadness Arrow Sudoku — 2025-10-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 6, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 2)], [(6, 2), (7, 1), (8, 0)])
    puzzle.add_arrow([(1, 8)], [(0, 7), (1, 7), (1, 6)])
    puzzle.add_arrow([(2, 6)], [(1, 5), (2, 4), (2, 3)])
    puzzle.add_arrow([(0, 3)], [(1, 2), (2, 1), (3, 1)])
    puzzle.add_arrow([(5, 7)], [(4, 7), (5, 8), (6, 7)])
    puzzle.add_arrow([(5, 1)], [(5, 0), (6, 1)])
    puzzle.add_arrow([(6, 5)], [(7, 4), (7, 5)])
    puzzle.add_arrow([(2, 5)], [(3, 4), (4, 4), (5, 3)])
    puzzle.add_arrow([(6, 6)], [(5, 5), (4, 5)])
    puzzle.add_arrow([(8, 7)], [(7, 7), (8, 8)])
    puzzle.add_arrow([(6, 0)], [(7, 0), (8, 1)])
    puzzle.add_arrow([(1, 3)], [(2, 2), (3, 3)])
    puzzle.add_arrow([(1, 0)], [(1, 1), (0, 1)])
    puzzle.add_arrow([(1, 4)], [(0, 5), (0, 6)])
    puzzle.add_arrow([(8, 4)], [(8, 3), (8, 2)])

    return puzzle
