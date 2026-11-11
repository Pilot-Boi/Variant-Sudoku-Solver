"""PuzzleMadness Arrow Sudoku — 2025-06-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-06-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/6/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 8, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 5)], [(6, 5), (6, 4)])
    puzzle.add_arrow([(0, 4)], [(1, 3), (2, 4), (2, 5)])
    puzzle.add_arrow([(5, 8)], [(5, 7), (4, 6), (3, 5)])
    puzzle.add_arrow([(0, 5)], [(1, 6), (1, 5)])
    puzzle.add_arrow([(2, 8)], [(3, 8), (4, 8)])
    puzzle.add_arrow([(6, 7)], [(7, 6), (6, 6), (5, 5)])
    puzzle.add_arrow([(8, 0)], [(8, 1), (8, 2), (7, 2)])
    puzzle.add_arrow([(7, 1)], [(6, 1), (5, 2), (4, 2)])
    puzzle.add_arrow([(1, 2)], [(2, 1), (2, 2)])
    puzzle.add_arrow([(8, 7)], [(8, 8), (7, 8)])
    puzzle.add_arrow([(4, 3)], [(5, 4), (4, 5)])
    puzzle.add_arrow([(5, 3)], [(6, 3), (6, 2)])
    puzzle.add_arrow([(4, 0)], [(4, 1), (3, 0)])
    puzzle.add_arrow([(0, 1)], [(1, 1), (0, 2)])
    puzzle.add_arrow([(7, 4)], [(8, 3), (8, 4)])
    puzzle.add_arrow([(1, 7)], [(0, 6), (0, 7)])
    puzzle.add_arrow([(2, 6)], [(3, 6), (4, 7)])
    puzzle.add_arrow([(3, 2)], [(3, 1), (2, 0)])

    return puzzle
