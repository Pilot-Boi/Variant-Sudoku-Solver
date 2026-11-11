"""PuzzleMadness Arrow Sudoku — 2025-09-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(8, 3)], [(8, 4), (7, 4), (8, 5)])
    puzzle.add_arrow([(6, 3)], [(5, 4), (4, 3)])
    puzzle.add_arrow([(1, 5)], [(2, 6), (1, 6)])
    puzzle.add_arrow([(2, 2)], [(1, 3), (1, 4), (0, 5)])
    puzzle.add_arrow([(8, 7)], [(7, 6), (6, 6)])
    puzzle.add_arrow([(4, 6)], [(3, 7), (3, 8), (2, 7)])
    puzzle.add_arrow([(8, 2)], [(8, 1), (7, 2)])
    puzzle.add_arrow([(1, 1)], [(1, 2), (2, 1)])
    puzzle.add_arrow([(5, 1)], [(5, 0), (6, 1), (6, 2)])
    puzzle.add_arrow([(4, 7)], [(5, 6), (4, 5)])
    puzzle.add_arrow([(3, 4)], [(3, 3), (2, 4), (2, 5)])
    puzzle.add_arrow([(0, 7)], [(0, 8), (1, 7), (2, 8)])
    puzzle.add_arrow([(2, 0)], [(3, 1), (4, 0)])
    puzzle.add_arrow([(4, 1)], [(5, 2), (4, 2)])
    puzzle.add_arrow([(4, 8)], [(5, 7), (5, 8)])
    puzzle.add_arrow([(7, 8)], [(7, 7), (8, 8)])
    puzzle.add_arrow([(0, 1)], [(1, 0), (0, 0)])
    puzzle.add_arrow([(6, 4)], [(7, 5), (8, 6)])

    return puzzle
