"""PuzzleMadness Arrow Sudoku — 2025-02-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 8, 0, 0, 9, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 5)], [(7, 4), (8, 5)])
    puzzle.add_arrow([(6, 6)], [(5, 5), (6, 5), (5, 6), (4, 7)])
    puzzle.add_arrow([(7, 0)], [(8, 1), (7, 2), (8, 3)])
    puzzle.add_arrow([(2, 1)], [(1, 1), (2, 0), (3, 1)])
    puzzle.add_arrow([(2, 8)], [(1, 7), (1, 6), (2, 5)])
    puzzle.add_arrow([(1, 5)], [(2, 6), (3, 7)])
    puzzle.add_arrow([(1, 4)], [(0, 4), (0, 5)])
    puzzle.add_arrow([(5, 0)], [(6, 0), (5, 1)])
    puzzle.add_arrow([(3, 3)], [(3, 2), (2, 2)])
    puzzle.add_arrow([(5, 7)], [(6, 7), (7, 6), (8, 6)])
    puzzle.add_arrow([(3, 8)], [(2, 7), (1, 8)])
    puzzle.add_arrow([(3, 5)], [(3, 4), (4, 3), (4, 2)])
    puzzle.add_arrow([(4, 8)], [(5, 8), (6, 8)])
    puzzle.add_arrow([(5, 2)], [(5, 3), (4, 4)])
    puzzle.add_arrow([(1, 3)], [(0, 3), (1, 2)])
    puzzle.add_arrow([(6, 3)], [(7, 3), (8, 2)])

    return puzzle
