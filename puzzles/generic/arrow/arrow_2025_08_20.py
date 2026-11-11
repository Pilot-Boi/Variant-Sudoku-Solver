"""PuzzleMadness Arrow Sudoku — 2025-08-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-08-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/8/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 9, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 5)], [(5, 5), (6, 4), (6, 5)])
    puzzle.add_arrow([(4, 3)], [(5, 3), (6, 2), (5, 2)])
    puzzle.add_arrow([(7, 7)], [(6, 7), (5, 6)])
    puzzle.add_arrow([(3, 2)], [(2, 2), (2, 1), (3, 0), (4, 1)])
    puzzle.add_arrow([(2, 6)], [(1, 7), (0, 7), (1, 6), (0, 5)])
    puzzle.add_arrow([(6, 3)], [(7, 4), (8, 3)])
    puzzle.add_arrow([(2, 8)], [(3, 7), (4, 8)])
    puzzle.add_arrow([(2, 4)], [(1, 4), (1, 3), (0, 4)])
    puzzle.add_arrow([(6, 1)], [(7, 1), (8, 1)])
    puzzle.add_arrow([(8, 5)], [(8, 6), (7, 5)])
    puzzle.add_arrow([(0, 0)], [(1, 0), (2, 0)])
    puzzle.add_arrow([(3, 6)], [(3, 5), (4, 6)])
    puzzle.add_arrow([(6, 0)], [(7, 0), (8, 0)])
    puzzle.add_arrow([(6, 6)], [(7, 6), (8, 7)])
    puzzle.add_arrow([(4, 7)], [(3, 8), (2, 7)])
    puzzle.add_arrow([(5, 7)], [(6, 8), (7, 8)])

    return puzzle
