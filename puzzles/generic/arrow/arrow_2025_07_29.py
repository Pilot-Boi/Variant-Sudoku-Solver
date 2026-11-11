"""PuzzleMadness Arrow Sudoku — 2025-07-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-07-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/7/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 3, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 0)], [(3, 1), (4, 2)])
    puzzle.add_arrow([(5, 5)], [(4, 5), (5, 6)])
    puzzle.add_arrow([(8, 5)], [(7, 6), (6, 7)])
    puzzle.add_arrow([(1, 2)], [(1, 3), (1, 4)])
    puzzle.add_arrow([(4, 4)], [(5, 3), (6, 4)])
    puzzle.add_arrow([(6, 1)], [(7, 0), (8, 0), (7, 1)])
    puzzle.add_arrow([(2, 0)], [(1, 1), (2, 1), (2, 2)])
    puzzle.add_arrow([(2, 5)], [(1, 6), (1, 7)])
    puzzle.add_arrow([(4, 6)], [(3, 7), (2, 7), (3, 8)])
    puzzle.add_arrow([(5, 1)], [(5, 0), (4, 0)])
    puzzle.add_arrow([(3, 6)], [(3, 5), (2, 4)])
    puzzle.add_arrow([(5, 4)], [(6, 3), (7, 4), (8, 4)])
    puzzle.add_arrow([(8, 7)], [(8, 8), (7, 8)])
    puzzle.add_arrow([(5, 8)], [(4, 7), (5, 7)])
    puzzle.add_arrow([(0, 5)], [(1, 5), (0, 4), (0, 3)])
    puzzle.add_arrow([(2, 3)], [(3, 2), (3, 3)])
    puzzle.add_arrow([(6, 2)], [(5, 2), (4, 3)])
    puzzle.add_arrow([(0, 7)], [(1, 8), (2, 8)])

    return puzzle
