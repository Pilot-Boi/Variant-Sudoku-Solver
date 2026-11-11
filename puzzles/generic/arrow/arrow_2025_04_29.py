"""PuzzleMadness Arrow Sudoku — 2025-04-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 0)], [(6, 1), (7, 2), (8, 2)])
    puzzle.add_arrow([(3, 2)], [(2, 3), (1, 4)])
    puzzle.add_arrow([(5, 3)], [(6, 3), (5, 4), (4, 4), (5, 5)])
    puzzle.add_arrow([(2, 7)], [(3, 6), (4, 6), (3, 7), (2, 6), (1, 5)])
    puzzle.add_arrow([(5, 0)], [(4, 0), (4, 1)])
    puzzle.add_arrow([(1, 2)], [(0, 2), (0, 3)])
    puzzle.add_arrow([(7, 6)], [(6, 5), (7, 5)])
    puzzle.add_arrow([(7, 4)], [(7, 3), (8, 4)])
    puzzle.add_arrow([(4, 7)], [(5, 7), (6, 8)])
    puzzle.add_arrow([(1, 8)], [(0, 7), (1, 6)])
    puzzle.add_arrow([(4, 3)], [(3, 4), (2, 4)])
    puzzle.add_arrow([(1, 1)], [(0, 0), (1, 0), (0, 1)])
    puzzle.add_arrow([(7, 7)], [(8, 7), (7, 8)])
    puzzle.add_arrow([(8, 1)], [(7, 1), (6, 0)])
    puzzle.add_arrow([(3, 1)], [(4, 2), (3, 3)])

    return puzzle
