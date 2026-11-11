"""PuzzleMadness Arrow Sudoku — 2025-11-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 7, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 6)], [(2, 6), (1, 5)])
    puzzle.add_arrow([(3, 3)], [(3, 4), (4, 4), (4, 5)])
    puzzle.add_arrow([(0, 5)], [(0, 6), (0, 7), (1, 8)])
    puzzle.add_arrow([(2, 4)], [(1, 4), (2, 3)])
    puzzle.add_arrow([(6, 5)], [(5, 5), (6, 6)])
    puzzle.add_arrow([(7, 8)], [(6, 8), (7, 7)])
    puzzle.add_arrow([(7, 1)], [(8, 2), (7, 3), (6, 4)])
    puzzle.add_arrow([(0, 0)], [(1, 1), (0, 2), (1, 2)])
    puzzle.add_arrow([(3, 1)], [(4, 0), (3, 0)])
    puzzle.add_arrow([(2, 7)], [(3, 7), (3, 6)])
    puzzle.add_arrow([(4, 3)], [(5, 4), (5, 3)])
    puzzle.add_arrow([(2, 2)], [(3, 2), (4, 1), (4, 2)])
    puzzle.add_arrow([(8, 6)], [(8, 7), (8, 8)])
    puzzle.add_arrow([(4, 7)], [(5, 7), (4, 8)])
    puzzle.add_arrow([(5, 0)], [(6, 0), (7, 0), (8, 0)])
    puzzle.add_arrow([(7, 4)], [(8, 5), (7, 5)])
    puzzle.add_arrow([(0, 8)], [(1, 7), (2, 8)])

    return puzzle
