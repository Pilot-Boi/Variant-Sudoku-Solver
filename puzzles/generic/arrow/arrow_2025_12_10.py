"""PuzzleMadness Arrow Sudoku — 2025-12-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-12-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/12/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 8, 0, 3, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 4)], [(3, 3), (4, 2), (5, 3), (6, 4)])
    puzzle.add_arrow([(5, 5)], [(6, 6), (5, 6), (5, 7), (5, 8)])
    puzzle.add_arrow([(1, 5)], [(1, 6), (0, 7)])
    puzzle.add_arrow([(3, 7)], [(4, 7), (4, 8)])
    puzzle.add_arrow([(0, 0)], [(0, 1), (1, 1), (1, 0)])
    puzzle.add_arrow([(6, 2)], [(7, 3), (7, 2)])
    puzzle.add_arrow([(7, 7)], [(7, 6), (6, 7)])
    puzzle.add_arrow([(4, 1)], [(3, 0), (3, 1), (3, 2)])
    puzzle.add_arrow([(6, 0)], [(6, 1), (7, 1)])
    puzzle.add_arrow([(3, 5)], [(2, 5), (1, 4)])
    puzzle.add_arrow([(5, 4)], [(4, 3), (5, 2)])
    puzzle.add_arrow([(8, 0)], [(8, 1), (7, 0)])
    puzzle.add_arrow([(2, 1)], [(2, 2), (2, 3)])
    puzzle.add_arrow([(1, 3)], [(0, 4), (0, 5)])
    puzzle.add_arrow([(2, 6)], [(2, 7), (1, 8)])
    puzzle.add_arrow([(7, 5)], [(8, 4), (8, 3)])

    return puzzle
