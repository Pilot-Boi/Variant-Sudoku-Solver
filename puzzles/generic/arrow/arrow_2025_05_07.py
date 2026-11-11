"""PuzzleMadness Arrow Sudoku — 2025-05-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-05-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/5/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 4)], [(4, 4), (3, 4)])
    puzzle.add_arrow([(0, 5)], [(0, 4), (1, 5), (0, 6)])
    puzzle.add_arrow([(3, 7)], [(2, 7), (1, 8), (0, 7)])
    puzzle.add_arrow([(7, 5)], [(8, 6), (8, 5), (7, 6), (6, 7)])
    puzzle.add_arrow([(2, 1)], [(3, 1), (4, 1), (3, 0), (2, 0)])
    puzzle.add_arrow([(6, 2)], [(5, 3), (6, 3), (6, 4)])
    puzzle.add_arrow([(1, 4)], [(2, 4), (2, 5)])
    puzzle.add_arrow([(7, 4)], [(8, 3), (7, 2)])
    puzzle.add_arrow([(5, 7)], [(5, 6), (5, 5)])
    puzzle.add_arrow([(4, 2)], [(5, 2), (4, 3)])
    puzzle.add_arrow([(8, 0)], [(8, 1), (8, 2)])
    puzzle.add_arrow([(1, 1)], [(1, 2), (0, 2)])
    puzzle.add_arrow([(6, 8)], [(7, 8), (7, 7)])
    puzzle.add_arrow([(2, 6)], [(3, 6), (4, 5)])
    puzzle.add_arrow([(5, 0)], [(6, 1), (6, 0)])
    puzzle.add_arrow([(4, 7)], [(3, 8), (2, 8)])

    return puzzle
