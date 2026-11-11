"""PuzzleMadness Arrow Sudoku — 2025-09-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 2, 0, 0, 0, 9, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(0, 6)], [(1, 7), (1, 8), (2, 8)])
    puzzle.add_arrow([(5, 7)], [(6, 7), (7, 6)])
    puzzle.add_arrow([(2, 6)], [(1, 5), (2, 4), (3, 4)])
    puzzle.add_arrow([(6, 4)], [(7, 4), (8, 3)])
    puzzle.add_arrow([(3, 3)], [(4, 3), (5, 2), (4, 1), (3, 0), (2, 1)])
    puzzle.add_arrow([(8, 5)], [(8, 4), (7, 5), (8, 6)])
    puzzle.add_arrow([(0, 3)], [(0, 2), (0, 1)])
    puzzle.add_arrow([(5, 8)], [(4, 8), (3, 8)])
    puzzle.add_arrow([(7, 3)], [(8, 2), (8, 1)])
    puzzle.add_arrow([(5, 5)], [(6, 6), (5, 6), (6, 5)])
    puzzle.add_arrow([(4, 2)], [(5, 1), (6, 2), (5, 3)])
    puzzle.add_arrow([(1, 0)], [(0, 0), (1, 1)])
    puzzle.add_arrow([(6, 1)], [(7, 1), (7, 0)])
    puzzle.add_arrow([(0, 4)], [(1, 3), (2, 3)])
    puzzle.add_arrow([(2, 5)], [(1, 6), (0, 5)])
    puzzle.add_arrow([(3, 6)], [(3, 7), (4, 7)])
    puzzle.add_arrow([(7, 8)], [(7, 7), (8, 8)])
    puzzle.add_arrow([(4, 5)], [(4, 4), (3, 5)])

    return puzzle
