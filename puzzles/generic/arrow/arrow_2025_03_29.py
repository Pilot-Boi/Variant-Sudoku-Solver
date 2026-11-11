"""PuzzleMadness Arrow Sudoku — 2025-03-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-03-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/3/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 5)], [(1, 4), (0, 5), (0, 4)])
    puzzle.add_arrow([(2, 1)], [(2, 0), (3, 1), (4, 1)])
    puzzle.add_arrow([(2, 7)], [(1, 7), (2, 6)])
    puzzle.add_arrow([(4, 4)], [(5, 4), (6, 3)])
    puzzle.add_arrow([(3, 4)], [(2, 3), (1, 3), (1, 2)])
    puzzle.add_arrow([(6, 4)], [(5, 5), (6, 5), (7, 4), (8, 3)])
    puzzle.add_arrow([(7, 6)], [(7, 7), (8, 7), (7, 8)])
    puzzle.add_arrow([(5, 2)], [(6, 1), (6, 0)])
    puzzle.add_arrow([(7, 1)], [(8, 1), (8, 0)])
    puzzle.add_arrow([(5, 6)], [(4, 7), (3, 8), (4, 8)])
    puzzle.add_arrow([(6, 8)], [(5, 7), (4, 6)])
    puzzle.add_arrow([(5, 3)], [(6, 2), (7, 2)])
    puzzle.add_arrow([(4, 0)], [(5, 1), (5, 0)])
    puzzle.add_arrow([(0, 3)], [(0, 2), (1, 1)])
    puzzle.add_arrow([(3, 3)], [(2, 4), (3, 5)])
    puzzle.add_arrow([(6, 6)], [(7, 5), (8, 6)])
    puzzle.add_arrow([(0, 7)], [(0, 6), (1, 6)])

    return puzzle
