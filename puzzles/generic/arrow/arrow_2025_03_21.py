"""PuzzleMadness Arrow Sudoku — 2025-03-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-03-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/3/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 9, 0],
        [7, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(6, 6)], [(5, 6), (6, 7)])
    puzzle.add_arrow([(6, 2)], [(7, 1), (7, 0), (6, 1)])
    puzzle.add_arrow([(2, 7)], [(1, 7), (0, 6)])
    puzzle.add_arrow([(4, 4)], [(5, 3), (4, 3)])
    puzzle.add_arrow([(3, 4)], [(3, 3), (2, 2), (1, 2)])
    puzzle.add_arrow([(1, 1)], [(1, 0), (2, 1)])
    puzzle.add_arrow([(7, 3)], [(6, 4), (7, 4)])
    puzzle.add_arrow([(2, 5)], [(3, 5), (2, 4), (1, 3), (0, 3)])
    puzzle.add_arrow([(5, 7)], [(4, 7), (4, 8)])
    puzzle.add_arrow([(8, 4)], [(7, 5), (8, 5)])
    puzzle.add_arrow([(1, 5)], [(1, 6), (0, 5)])
    puzzle.add_arrow([(3, 6)], [(4, 5), (5, 4)])
    puzzle.add_arrow([(7, 6)], [(8, 6), (7, 7), (6, 8)])
    puzzle.add_arrow([(4, 1)], [(3, 0), (3, 1)])
    puzzle.add_arrow([(8, 0)], [(8, 1), (7, 2), (8, 3)])
    puzzle.add_arrow([(2, 3)], [(1, 4), (0, 4)])
    puzzle.add_arrow([(4, 0)], [(5, 0), (6, 0)])
    puzzle.add_arrow([(3, 2)], [(4, 2), (5, 2)])

    return puzzle
