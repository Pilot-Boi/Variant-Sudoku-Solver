"""PuzzleMadness Between Lines Sudoku — 2025-02-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 4, 0, 0, 0, 0],
        [0, 2, 0, 8, 7, 0, 0, 4, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 5, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 2],
        [8, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 8), (1, 8), (1, 7), (2, 7), (3, 8), (2, 8)])
    puzzle.add_between_line([(8, 5), (8, 4), (7, 5), (6, 5), (5, 4)])
    puzzle.add_between_line([(6, 0), (6, 1), (5, 2), (6, 3), (6, 2)])
    puzzle.add_between_line([(7, 7), (7, 8), (6, 7), (5, 7), (6, 8)])
    puzzle.add_between_line([(4, 1), (3, 2), (3, 1), (3, 0)])
    puzzle.add_between_line([(0, 3), (1, 3), (1, 4), (1, 5)])
    puzzle.add_between_line([(7, 2), (7, 1), (8, 2), (8, 3)])
    puzzle.add_between_line([(4, 6), (4, 7), (4, 8)])
    puzzle.add_between_line([(5, 3), (4, 4), (4, 3)])
    puzzle.add_between_line([(7, 3), (6, 4), (7, 4)])

    return puzzle
