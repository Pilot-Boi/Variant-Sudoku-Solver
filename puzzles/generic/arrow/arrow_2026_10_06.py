"""PuzzleMadness Arrow Sudoku — 2026-10-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2026-10-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2026/10/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 4)], [(2, 5), (1, 4), (1, 3)])
    puzzle.add_arrow([(7, 4)], [(7, 3), (8, 2)])
    puzzle.add_arrow([(7, 6)], [(6, 7), (5, 7), (4, 6), (3, 5)])
    puzzle.add_arrow([(5, 8)], [(6, 8), (7, 7)])
    puzzle.add_arrow([(6, 3)], [(6, 2), (5, 3)])
    puzzle.add_arrow([(4, 0)], [(3, 1), (2, 2)])
    puzzle.add_arrow([(4, 3)], [(3, 3), (3, 2)])
    puzzle.add_arrow([(6, 5)], [(7, 5), (6, 4), (5, 5)])
    puzzle.add_arrow([(1, 1)], [(1, 0), (0, 1)])
    puzzle.add_arrow([(0, 5)], [(0, 4), (1, 5)])
    puzzle.add_arrow([(4, 2)], [(5, 1), (4, 1)])
    puzzle.add_arrow([(3, 7)], [(2, 6), (1, 7), (0, 8)])
    puzzle.add_arrow([(7, 0)], [(8, 1), (7, 2)])
    puzzle.add_arrow([(3, 6)], [(4, 7), (5, 6)])

    return puzzle
