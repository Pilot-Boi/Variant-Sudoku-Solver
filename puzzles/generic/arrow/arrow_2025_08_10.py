"""PuzzleMadness Arrow Sudoku — 2025-08-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-08-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/8/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 6, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 1)], [(5, 1), (6, 1), (6, 0)])
    puzzle.add_arrow([(2, 3)], [(2, 4), (1, 5), (2, 5)])
    puzzle.add_arrow([(6, 4)], [(7, 4), (6, 5)])
    puzzle.add_arrow([(0, 3)], [(1, 2), (0, 1)])
    puzzle.add_arrow([(3, 7)], [(2, 8), (1, 7), (0, 7)])
    puzzle.add_arrow([(3, 3)], [(4, 3), (5, 4)])
    puzzle.add_arrow([(5, 7)], [(5, 6), (4, 6), (3, 6)])
    puzzle.add_arrow([(2, 6)], [(2, 7), (1, 8)])
    puzzle.add_arrow([(7, 5)], [(8, 6), (7, 6), (8, 7)])
    puzzle.add_arrow([(6, 8)], [(7, 7), (7, 8)])
    puzzle.add_arrow([(4, 4)], [(3, 5), (3, 4)])
    puzzle.add_arrow([(7, 2)], [(6, 3), (5, 3), (4, 2)])
    puzzle.add_arrow([(7, 1)], [(7, 0), (8, 1), (8, 0)])
    puzzle.add_arrow([(2, 2)], [(1, 1), (0, 2)])
    puzzle.add_arrow([(8, 2)], [(7, 3), (8, 4)])
    puzzle.add_arrow([(4, 0)], [(3, 0), (3, 1)])
    puzzle.add_arrow([(5, 8)], [(4, 8), (3, 8)])

    return puzzle
