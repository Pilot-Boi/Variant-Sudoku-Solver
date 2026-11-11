"""PuzzleMadness Arrow Sudoku — 2025-09-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 6, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 6)], [(1, 6), (0, 7)])
    puzzle.add_arrow([(3, 3)], [(2, 3), (2, 2), (3, 1)])
    puzzle.add_arrow([(3, 6)], [(4, 6), (3, 5)])
    puzzle.add_arrow([(5, 4)], [(4, 5), (4, 4), (4, 3), (5, 2)])
    puzzle.add_arrow([(6, 5)], [(7, 6), (8, 6)])
    puzzle.add_arrow([(8, 3)], [(7, 4), (7, 3)])
    puzzle.add_arrow([(5, 0)], [(6, 0), (7, 0), (8, 1)])
    puzzle.add_arrow([(6, 7)], [(5, 6), (5, 7)])
    puzzle.add_arrow([(0, 4)], [(1, 5), (0, 6)])
    puzzle.add_arrow([(1, 3)], [(1, 4), (0, 3)])
    puzzle.add_arrow([(1, 7)], [(2, 7), (1, 8), (0, 8)])
    puzzle.add_arrow([(7, 7)], [(6, 8), (7, 8)])
    puzzle.add_arrow([(3, 2)], [(4, 2), (5, 3)])
    puzzle.add_arrow([(4, 7)], [(3, 7), (3, 8)])
    puzzle.add_arrow([(1, 1)], [(0, 0), (0, 1)])
    puzzle.add_arrow([(4, 1)], [(3, 0), (2, 1)])
    puzzle.add_arrow([(6, 3)], [(6, 4), (5, 5)])
    puzzle.add_arrow([(7, 5)], [(8, 5), (8, 4)])

    return puzzle
