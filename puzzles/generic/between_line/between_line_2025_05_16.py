"""PuzzleMadness Between Lines Sudoku — 2025-05-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 4, 5, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 3, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 8, 0, 2],
        [0, 7, 0, 0, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 5), (2, 5), (1, 5), (1, 4), (0, 4), (0, 5)])
    puzzle.add_between_line([(5, 5), (6, 6), (7, 5), (8, 5), (8, 4)])
    puzzle.add_between_line([(4, 6), (3, 7), (2, 8), (1, 7), (1, 6)])
    puzzle.add_between_line([(6, 8), (7, 7), (8, 6), (7, 6), (6, 7)])
    puzzle.add_between_line([(4, 2), (3, 3), (2, 3), (2, 2)])
    puzzle.add_between_line([(3, 2), (2, 1), (1, 2), (0, 3)])
    puzzle.add_between_line([(7, 3), (6, 2), (5, 1), (4, 0)])
    puzzle.add_between_line([(4, 8), (5, 7), (4, 7), (5, 6)])
    puzzle.add_between_line([(7, 2), (8, 1), (7, 1)])
    puzzle.add_between_line([(8, 3), (7, 4), (6, 5)])
    puzzle.add_between_line([(5, 0), (6, 0), (7, 0)])
    puzzle.add_between_line([(0, 6), (0, 7), (0, 8)])

    return puzzle
