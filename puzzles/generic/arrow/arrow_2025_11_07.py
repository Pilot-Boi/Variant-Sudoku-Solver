"""PuzzleMadness Arrow Sudoku — 2025-11-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 9, 0, 0, 0, 5, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(3, 5)], [(4, 5), (4, 4), (3, 4)])
    puzzle.add_arrow([(1, 1)], [(0, 1), (0, 0)])
    puzzle.add_arrow([(4, 7)], [(5, 7), (6, 8)])
    puzzle.add_arrow([(5, 5)], [(5, 6), (6, 5), (7, 6), (7, 5)])
    puzzle.add_arrow([(8, 1)], [(7, 0), (6, 0), (7, 1)])
    puzzle.add_arrow([(0, 8)], [(1, 7), (2, 7), (3, 7), (4, 8)])
    puzzle.add_arrow([(5, 2)], [(4, 3), (3, 3), (2, 3)])
    puzzle.add_arrow([(7, 7)], [(8, 8), (7, 8)])
    puzzle.add_arrow([(5, 3)], [(4, 2), (3, 1), (3, 2)])
    puzzle.add_arrow([(7, 3)], [(8, 4), (8, 5)])
    puzzle.add_arrow([(3, 0)], [(4, 1), (5, 1)])
    puzzle.add_arrow([(2, 4)], [(1, 4), (0, 5)])
    puzzle.add_arrow([(2, 2)], [(2, 1), (1, 0)])
    puzzle.add_arrow([(1, 2)], [(1, 3), (0, 2)])

    return puzzle
