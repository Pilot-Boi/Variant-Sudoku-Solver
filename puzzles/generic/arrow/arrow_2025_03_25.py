"""PuzzleMadness Arrow Sudoku — 2025-03-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-03-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/3/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 8)], [(5, 7), (6, 7), (5, 6), (4, 6)])
    puzzle.add_arrow([(0, 5)], [(1, 6), (1, 5)])
    puzzle.add_arrow([(4, 2)], [(4, 3), (5, 4), (6, 5)])
    puzzle.add_arrow([(8, 0)], [(7, 1), (7, 2), (6, 1)])
    puzzle.add_arrow([(2, 3)], [(3, 3), (2, 2), (3, 2), (2, 1)])
    puzzle.add_arrow([(2, 0)], [(3, 1), (4, 0)])
    puzzle.add_arrow([(2, 5)], [(2, 6), (2, 7)])
    puzzle.add_arrow([(1, 4)], [(0, 4), (1, 3)])
    puzzle.add_arrow([(6, 3)], [(7, 4), (6, 4)])
    puzzle.add_arrow([(0, 1)], [(1, 0), (0, 0)])
    puzzle.add_arrow([(6, 6)], [(7, 6), (7, 5)])
    puzzle.add_arrow([(7, 7)], [(8, 7), (8, 6)])
    puzzle.add_arrow([(0, 8)], [(1, 7), (0, 7)])
    puzzle.add_arrow([(7, 0)], [(8, 1), (8, 2)])
    puzzle.add_arrow([(3, 6)], [(3, 5), (2, 4)])

    return puzzle
