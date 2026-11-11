"""PuzzleMadness Arrow Sudoku — 2025-10-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 4)], [(6, 4), (5, 5), (4, 6)])
    puzzle.add_arrow([(6, 7)], [(6, 8), (7, 8), (7, 7)])
    puzzle.add_arrow([(2, 5)], [(1, 5), (2, 4)])
    puzzle.add_arrow([(5, 8)], [(4, 7), (5, 7), (5, 6)])
    puzzle.add_arrow([(4, 4)], [(4, 3), (3, 2), (2, 1)])
    puzzle.add_arrow([(5, 1)], [(4, 2), (3, 1)])
    puzzle.add_arrow([(0, 7)], [(1, 7), (2, 7)])
    puzzle.add_arrow([(4, 0)], [(4, 1), (3, 0)])
    puzzle.add_arrow([(6, 3)], [(7, 3), (7, 2)])
    puzzle.add_arrow([(0, 5)], [(1, 4), (1, 3)])
    puzzle.add_arrow([(0, 2)], [(0, 1), (1, 1)])
    puzzle.add_arrow([(4, 8)], [(3, 8), (2, 8)])
    puzzle.add_arrow([(7, 1)], [(8, 0), (7, 0)])
    puzzle.add_arrow([(7, 6)], [(6, 5), (7, 5)])
    puzzle.add_arrow([(3, 7)], [(3, 6), (3, 5)])
    puzzle.add_arrow([(8, 6)], [(8, 5), (8, 4)])

    return puzzle
