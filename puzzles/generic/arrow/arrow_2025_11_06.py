"""PuzzleMadness Arrow Sudoku — 2025-11-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 1, 0, 0, 9],
        [2, 0, 0, 0, 0, 0, 0, 0, 7],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 7)], [(4, 6), (5, 7)])
    puzzle.add_arrow([(1, 0)], [(2, 0), (2, 1), (1, 2)])
    puzzle.add_arrow([(5, 5)], [(4, 4), (5, 3), (4, 3)])
    puzzle.add_arrow([(2, 5)], [(1, 4), (1, 5)])
    puzzle.add_arrow([(7, 3)], [(8, 3), (8, 2)])
    puzzle.add_arrow([(7, 6)], [(8, 6), (7, 5)])
    puzzle.add_arrow([(3, 4)], [(3, 5), (4, 5)])
    puzzle.add_arrow([(5, 1)], [(6, 1), (6, 0)])
    puzzle.add_arrow([(4, 0)], [(4, 1), (5, 2), (6, 3)])
    puzzle.add_arrow([(6, 4)], [(7, 4), (6, 5)])
    puzzle.add_arrow([(1, 1)], [(0, 1), (0, 0)])
    puzzle.add_arrow([(7, 8)], [(6, 8), (5, 8)])
    puzzle.add_arrow([(1, 8)], [(2, 7), (1, 7), (1, 6)])
    puzzle.add_arrow([(3, 1)], [(3, 2), (3, 3)])
    puzzle.add_arrow([(8, 1)], [(7, 1), (7, 0)])
    puzzle.add_arrow([(2, 3)], [(1, 3), (0, 3)])
    puzzle.add_arrow([(6, 6)], [(7, 7), (8, 8)])

    return puzzle
