"""PuzzleMadness Between Lines Sudoku — 2025-04-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 7, 1, 0, 0, 0],
        [0, 0, 6, 8, 0, 0, 3, 0, 7],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 5, 0, 0, 9, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 4), (0, 3), (0, 4), (1, 5), (2, 6), (3, 5)])
    puzzle.add_between_line([(5, 1), (6, 2), (7, 1), (7, 2), (8, 2)])
    puzzle.add_between_line([(3, 6), (4, 7), (5, 6), (6, 6), (5, 7)])
    puzzle.add_between_line([(5, 4), (4, 5), (5, 5), (6, 4), (7, 5)])
    puzzle.add_between_line([(0, 2), (1, 2), (1, 1), (2, 2), (1, 3)])
    puzzle.add_between_line([(0, 6), (1, 6), (0, 7), (1, 8)])
    puzzle.add_between_line([(4, 2), (3, 2), (3, 1), (4, 1)])
    puzzle.add_between_line([(3, 8), (4, 8), (5, 8), (6, 7)])
    puzzle.add_between_line([(8, 4), (7, 3), (6, 3), (5, 3)])
    puzzle.add_between_line([(7, 0), (6, 0), (6, 1)])
    puzzle.add_between_line([(2, 0), (1, 0), (0, 0)])
    puzzle.add_between_line([(2, 4), (3, 4), (2, 3)])

    return puzzle
