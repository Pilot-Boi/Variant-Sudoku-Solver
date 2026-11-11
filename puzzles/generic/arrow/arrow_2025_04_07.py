"""PuzzleMadness Arrow Sudoku — 2025-04-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 5, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 5)], [(3, 6), (3, 5)])
    puzzle.add_arrow([(7, 3)], [(6, 2), (6, 3)])
    puzzle.add_arrow([(8, 6)], [(7, 6), (6, 6)])
    puzzle.add_arrow([(2, 3)], [(1, 3), (0, 3)])
    puzzle.add_arrow([(0, 8)], [(1, 7), (2, 7)])
    puzzle.add_arrow([(3, 0)], [(4, 1), (5, 1)])
    puzzle.add_arrow([(3, 2)], [(3, 3), (4, 4)])
    puzzle.add_arrow([(8, 5)], [(7, 5), (7, 4), (6, 5)])
    puzzle.add_arrow([(2, 2)], [(3, 1), (2, 0)])
    puzzle.add_arrow([(5, 5)], [(5, 6), (4, 7), (3, 8)])
    puzzle.add_arrow([(3, 4)], [(4, 3), (5, 3)])
    puzzle.add_arrow([(0, 4)], [(0, 5), (1, 5), (1, 6)])
    puzzle.add_arrow([(1, 1)], [(0, 2), (0, 1)])
    puzzle.add_arrow([(6, 1)], [(7, 0), (8, 1)])
    puzzle.add_arrow([(7, 8)], [(8, 8), (7, 7), (6, 7)])
    puzzle.add_arrow([(4, 8)], [(5, 7), (6, 8)])

    return puzzle
