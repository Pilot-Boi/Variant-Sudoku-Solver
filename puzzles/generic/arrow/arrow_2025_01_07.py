"""PuzzleMadness Arrow Sudoku — 2025-01-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 4, 0, 3],
        [4, 0, 0, 2, 0, 0, 7, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 4, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(0, 0)], [(1, 1), (0, 1)])
    puzzle.add_arrow([(7, 6)], [(8, 5), (8, 6), (7, 7)])
    puzzle.add_arrow([(5, 2)], [(6, 3), (5, 3)])
    puzzle.add_arrow([(1, 4)], [(2, 5), (2, 6)])
    puzzle.add_arrow([(1, 8)], [(0, 7), (0, 8)])
    puzzle.add_arrow([(7, 0)], [(6, 0), (6, 1)])
    puzzle.add_arrow([(4, 0)], [(5, 0), (4, 1)])
    puzzle.add_arrow([(2, 2)], [(3, 1), (4, 2)])
    puzzle.add_arrow([(3, 5)], [(3, 4), (4, 4), (5, 4)])
    puzzle.add_arrow([(0, 3)], [(1, 3), (1, 2), (2, 1)])
    puzzle.add_arrow([(5, 7)], [(5, 6), (4, 7)])
    puzzle.add_arrow([(6, 7)], [(6, 8), (5, 8)])
    puzzle.add_arrow([(8, 2)], [(8, 3), (7, 3), (6, 2)])
    puzzle.add_arrow([(2, 8)], [(3, 7), (2, 7)])
    puzzle.add_arrow([(7, 4)], [(6, 5), (5, 5)])

    return puzzle
