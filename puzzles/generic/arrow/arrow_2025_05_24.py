"""PuzzleMadness Arrow Sudoku — 2025-05-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-05-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/5/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 1)], [(8, 2), (7, 3), (6, 4)])
    puzzle.add_arrow([(5, 3)], [(4, 3), (5, 2)])
    puzzle.add_arrow([(4, 8)], [(3, 7), (2, 6), (2, 7)])
    puzzle.add_arrow([(3, 2)], [(2, 1), (3, 0)])
    puzzle.add_arrow([(1, 6)], [(0, 5), (0, 4), (1, 3)])
    puzzle.add_arrow([(6, 8)], [(5, 7), (5, 6), (6, 5)])
    puzzle.add_arrow([(4, 2)], [(4, 1), (5, 0), (4, 0)])
    puzzle.add_arrow([(0, 1)], [(1, 2), (0, 2)])
    puzzle.add_arrow([(3, 3)], [(2, 3), (3, 4)])
    puzzle.add_arrow([(3, 5)], [(2, 5), (3, 6)])
    puzzle.add_arrow([(7, 5)], [(7, 6), (6, 7), (5, 8)])
    puzzle.add_arrow([(6, 1)], [(7, 2), (6, 2)])
    puzzle.add_arrow([(0, 7)], [(1, 7), (1, 8)])
    puzzle.add_arrow([(5, 4)], [(4, 4), (4, 5)])
    puzzle.add_arrow([(2, 0)], [(1, 0), (0, 0)])
    puzzle.add_arrow([(8, 7)], [(7, 8), (7, 7), (8, 6)])
    puzzle.add_arrow([(7, 0)], [(8, 1), (8, 0)])
    puzzle.add_arrow([(8, 4)], [(7, 4), (6, 3)])
    puzzle.add_arrow([(4, 7)], [(4, 6), (5, 5)])

    return puzzle
