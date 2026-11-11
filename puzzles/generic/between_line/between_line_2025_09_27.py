"""PuzzleMadness Between Lines Sudoku — 2025-09-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 1, 0, 8, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 1],
        [0, 0, 8, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 3), (0, 4), (1, 5), (1, 4), (2, 4), (2, 5)])
    puzzle.add_between_line([(4, 2), (4, 3), (3, 2), (3, 1), (2, 1)])
    puzzle.add_between_line([(7, 3), (6, 3), (5, 3), (6, 2), (5, 1)])
    puzzle.add_between_line([(4, 4), (5, 5), (6, 4), (7, 4), (8, 4)])
    puzzle.add_between_line([(8, 7), (7, 7), (6, 7), (5, 7), (6, 8)])
    puzzle.add_between_line([(2, 3), (3, 4), (3, 3), (2, 2)])
    puzzle.add_between_line([(1, 1), (1, 0), (0, 1), (0, 0)])
    puzzle.add_between_line([(8, 3), (7, 2), (7, 1), (6, 0)])
    puzzle.add_between_line([(3, 5), (4, 6), (3, 7)])
    puzzle.add_between_line([(8, 2), (8, 1), (8, 0)])
    puzzle.add_between_line([(4, 8), (4, 7), (5, 8)])

    return puzzle
