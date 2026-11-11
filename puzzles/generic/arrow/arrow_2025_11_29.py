"""PuzzleMadness Arrow Sudoku — 2025-11-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 4)], [(5, 5), (6, 4), (7, 4)])
    puzzle.add_arrow([(2, 5)], [(3, 5), (2, 4), (1, 3), (2, 2)])
    puzzle.add_arrow([(4, 6)], [(4, 7), (3, 6), (2, 6), (1, 7)])
    puzzle.add_arrow([(2, 0)], [(3, 1), (4, 1)])
    puzzle.add_arrow([(7, 5)], [(8, 5), (8, 4)])
    puzzle.add_arrow([(3, 8)], [(4, 8), (5, 8)])
    puzzle.add_arrow([(6, 0)], [(5, 0), (4, 0), (3, 0)])
    puzzle.add_arrow([(2, 1)], [(1, 2), (0, 2)])
    puzzle.add_arrow([(1, 4)], [(0, 3), (0, 4)])
    puzzle.add_arrow([(1, 6)], [(0, 6), (0, 5)])
    puzzle.add_arrow([(7, 3)], [(7, 2), (6, 2), (7, 1)])
    puzzle.add_arrow([(7, 7)], [(7, 6), (6, 5)])
    puzzle.add_arrow([(6, 7)], [(7, 8), (6, 8)])
    puzzle.add_arrow([(6, 1)], [(7, 0), (8, 1)])
    puzzle.add_arrow([(4, 4)], [(5, 3), (4, 2)])
    puzzle.add_arrow([(0, 8)], [(1, 8), (2, 8)])
    puzzle.add_arrow([(0, 0)], [(1, 0), (0, 1)])

    return puzzle
