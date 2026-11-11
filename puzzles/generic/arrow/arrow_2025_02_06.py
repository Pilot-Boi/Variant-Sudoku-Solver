"""PuzzleMadness Arrow Sudoku — 2025-02-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 5)], [(1, 6), (2, 5), (3, 5)])
    puzzle.add_arrow([(5, 4)], [(5, 5), (5, 6)])
    puzzle.add_arrow([(4, 2)], [(3, 3), (2, 4), (1, 4), (0, 4)])
    puzzle.add_arrow([(6, 0)], [(6, 1), (7, 1), (8, 2)])
    puzzle.add_arrow([(2, 0)], [(3, 0), (4, 0), (4, 1)])
    puzzle.add_arrow([(7, 3)], [(6, 3), (7, 4), (7, 5)])
    puzzle.add_arrow([(4, 6)], [(3, 7), (2, 8)])
    puzzle.add_arrow([(2, 1)], [(1, 2), (0, 3), (0, 2)])
    puzzle.add_arrow([(4, 5)], [(4, 4), (4, 3)])
    puzzle.add_arrow([(7, 7)], [(7, 6), (8, 5)])
    puzzle.add_arrow([(5, 7)], [(6, 7), (7, 8), (8, 7)])
    puzzle.add_arrow([(3, 1)], [(2, 2), (1, 3)])
    puzzle.add_arrow([(2, 7)], [(1, 7), (0, 8)])
    puzzle.add_arrow([(8, 1)], [(7, 0), (8, 0)])
    puzzle.add_arrow([(3, 8)], [(4, 7), (5, 8)])
    puzzle.add_arrow([(5, 2)], [(5, 1), (5, 0)])

    return puzzle
