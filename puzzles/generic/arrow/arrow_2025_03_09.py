"""PuzzleMadness Arrow Sudoku — 2025-03-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-03-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/3/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 5, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(4, 5)], [(5, 5), (5, 6), (5, 7)])
    puzzle.add_arrow([(0, 3)], [(1, 3), (1, 4), (1, 5)])
    puzzle.add_arrow([(1, 8)], [(0, 7), (0, 6), (1, 6), (2, 5)])
    puzzle.add_arrow([(7, 5)], [(8, 6), (8, 5), (7, 4), (6, 3)])
    puzzle.add_arrow([(2, 6)], [(1, 7), (0, 8)])
    puzzle.add_arrow([(8, 7)], [(7, 8), (7, 7)])
    puzzle.add_arrow([(6, 0)], [(7, 1), (8, 2)])
    puzzle.add_arrow([(7, 2)], [(6, 2), (5, 3)])
    puzzle.add_arrow([(3, 0)], [(3, 1), (4, 2)])
    puzzle.add_arrow([(4, 8)], [(3, 7), (3, 8)])
    puzzle.add_arrow([(2, 4)], [(3, 3), (4, 3)])
    puzzle.add_arrow([(0, 2)], [(1, 1), (2, 0)])
    puzzle.add_arrow([(5, 1)], [(4, 0), (4, 1)])
    puzzle.add_arrow([(1, 2)], [(2, 3), (3, 4)])

    return puzzle
