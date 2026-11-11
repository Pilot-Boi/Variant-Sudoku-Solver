"""PuzzleMadness Between Lines Sudoku — 2025-05-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 1, 0, 0, 0],
        [0, 0, 0, 9, 8, 0, 0, 0, 0],
        [3, 0, 0, 6, 0, 9, 0, 0, 0],
        [0, 0, 0, 5, 2, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 7, 0, 0],
        [9, 0, 0, 0, 4, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 2), (6, 2), (7, 3), (8, 2), (8, 1), (8, 0)])
    puzzle.add_between_line([(4, 1), (3, 0), (3, 1), (4, 2), (3, 2)])
    puzzle.add_between_line([(2, 6), (1, 6), (2, 7), (3, 6), (4, 6)])
    puzzle.add_between_line([(6, 1), (5, 1), (4, 0), (5, 0), (6, 0)])
    puzzle.add_between_line([(0, 7), (0, 8), (1, 7), (0, 6)])
    puzzle.add_between_line([(3, 7), (3, 8), (4, 8), (5, 8)])
    puzzle.add_between_line([(0, 1), (1, 2), (1, 3), (0, 3)])
    puzzle.add_between_line([(6, 4), (6, 5), (5, 4), (4, 4)])
    puzzle.add_between_line([(0, 0), (1, 0), (1, 1)])
    puzzle.add_between_line([(5, 7), (4, 7), (5, 6)])
    puzzle.add_between_line([(2, 5), (2, 4), (2, 3)])

    return puzzle
