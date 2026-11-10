"""PuzzleMadness Arrow Sudoku — 2026-10-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2026-10-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2026/10/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 7, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 1)], [(1, 2), (2, 1), (3, 1), (3, 0)])
    puzzle.add_arrow([(6, 4)], [(7, 3), (6, 2)])
    puzzle.add_arrow([(0, 5)], [(1, 4), (1, 3)])
    puzzle.add_arrow([(4, 7)], [(5, 8), (5, 7), (4, 6), (4, 5)])
    puzzle.add_arrow([(5, 4)], [(5, 5), (4, 4)])
    puzzle.add_arrow([(7, 2)], [(8, 3), (8, 4)])
    puzzle.add_arrow([(3, 6)], [(2, 7), (3, 8)])
    puzzle.add_arrow([(1, 7)], [(0, 6), (0, 7)])
    puzzle.add_arrow([(6, 0)], [(6, 1), (7, 0)])
    puzzle.add_arrow([(7, 7)], [(8, 6), (7, 5)])
    puzzle.add_arrow([(4, 0)], [(5, 1), (4, 1)])
    puzzle.add_arrow([(2, 3)], [(2, 4), (3, 3)])
    puzzle.add_arrow([(7, 4)], [(6, 3), (5, 3)])
    puzzle.add_arrow([(8, 2)], [(8, 1), (7, 1)])
    puzzle.add_arrow([(5, 6)], [(6, 7), (6, 8)])
    puzzle.add_arrow([(2, 8)], [(3, 7), (4, 8)])
    puzzle.add_arrow([(8, 7)], [(7, 6), (6, 5)])
    puzzle.add_arrow([(3, 5)], [(2, 5), (3, 4)])
    puzzle.add_arrow([(4, 2)], [(3, 2), (2, 2)])

    return puzzle
