"""PuzzleMadness Arrow Sudoku — 2025-04-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-04-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/4/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 6)], [(6, 6), (5, 7), (4, 6), (4, 5), (5, 4)])
    puzzle.add_arrow([(7, 1)], [(7, 0), (6, 1), (5, 1)])
    puzzle.add_arrow([(3, 3)], [(2, 3), (1, 2), (0, 2)])
    puzzle.add_arrow([(2, 5)], [(3, 5), (3, 6), (3, 7)])
    puzzle.add_arrow([(2, 1)], [(2, 0), (1, 1)])
    puzzle.add_arrow([(8, 6)], [(8, 7), (7, 7)])
    puzzle.add_arrow([(8, 4)], [(8, 5), (7, 4), (7, 3)])
    puzzle.add_arrow([(4, 2)], [(5, 2), (4, 1), (4, 0)])
    puzzle.add_arrow([(5, 3)], [(6, 4), (5, 5)])
    puzzle.add_arrow([(0, 3)], [(1, 3), (0, 4)])
    puzzle.add_arrow([(1, 4)], [(1, 5), (0, 5)])
    puzzle.add_arrow([(6, 2)], [(7, 2), (8, 3)])
    puzzle.add_arrow([(0, 6)], [(1, 7), (2, 8)])
    puzzle.add_arrow([(6, 7)], [(6, 8), (5, 8)])
    puzzle.add_arrow([(3, 8)], [(2, 7), (1, 6)])

    return puzzle
