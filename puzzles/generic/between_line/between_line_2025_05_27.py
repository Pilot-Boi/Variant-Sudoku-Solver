"""PuzzleMadness Between Lines Sudoku — 2025-05-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 1, 0, 5, 0, 4, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 9, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 8), (2, 8), (1, 8), (0, 7), (1, 7), (2, 7)])
    puzzle.add_between_line([(5, 4), (6, 4), (6, 3), (7, 2), (6, 1)])
    puzzle.add_between_line([(3, 4), (2, 3), (1, 2), (0, 3), (1, 4)])
    puzzle.add_between_line([(3, 7), (4, 7), (5, 7), (6, 7), (7, 7)])
    puzzle.add_between_line([(4, 6), (5, 5), (4, 4), (4, 3)])
    puzzle.add_between_line([(1, 6), (2, 5), (1, 5), (2, 4)])
    puzzle.add_between_line([(5, 2), (4, 1), (3, 1), (4, 0)])
    puzzle.add_between_line([(2, 1), (1, 0), (0, 1), (1, 1)])
    puzzle.add_between_line([(8, 6), (7, 6), (7, 5)])
    puzzle.add_between_line([(6, 5), (7, 4), (8, 5)])
    puzzle.add_between_line([(7, 8), (6, 8), (5, 8)])

    return puzzle
