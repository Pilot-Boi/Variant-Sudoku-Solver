"""PuzzleMadness Arrow Sudoku — 2025-03-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-03-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/3/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(8, 0)], [(8, 1), (7, 0)])
    puzzle.add_arrow([(5, 6)], [(5, 5), (6, 6)])
    puzzle.add_arrow([(3, 5)], [(4, 5), (3, 4), (2, 3)])
    puzzle.add_arrow([(6, 3)], [(5, 4), (6, 5)])
    puzzle.add_arrow([(3, 6)], [(2, 6), (3, 7), (3, 8)])
    puzzle.add_arrow([(1, 2)], [(1, 1), (0, 2), (1, 3), (0, 3)])
    puzzle.add_arrow([(4, 1)], [(3, 2), (2, 2)])
    puzzle.add_arrow([(7, 7)], [(7, 6), (8, 7), (8, 8)])
    puzzle.add_arrow([(7, 1)], [(6, 0), (5, 0), (6, 1)])
    puzzle.add_arrow([(8, 3)], [(7, 4), (6, 4), (7, 3)])
    puzzle.add_arrow([(5, 2)], [(5, 1), (4, 0)])
    puzzle.add_arrow([(2, 4)], [(1, 5), (0, 5)])
    puzzle.add_arrow([(2, 5)], [(1, 6), (2, 7)])
    puzzle.add_arrow([(4, 8)], [(4, 7), (4, 6)])
    puzzle.add_arrow([(0, 6)], [(0, 7), (1, 8)])
    puzzle.add_arrow([(6, 8)], [(5, 7), (6, 7)])
    puzzle.add_arrow([(4, 4)], [(5, 3), (4, 2)])
    puzzle.add_arrow([(0, 0)], [(1, 0), (2, 0)])

    return puzzle
