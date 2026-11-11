"""PuzzleMadness Between Lines Sudoku — 2025-11-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 7, 9, 0, 0],
        [8, 0, 0, 3, 0, 4, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 9, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 1), (6, 2), (7, 3), (7, 4), (7, 5), (8, 4)])
    puzzle.add_between_line([(2, 4), (2, 5), (1, 6), (1, 7), (2, 6)])
    puzzle.add_between_line([(0, 5), (0, 4), (1, 3), (0, 2), (0, 3)])
    puzzle.add_between_line([(3, 8), (4, 7), (4, 6), (3, 5), (4, 4)])
    puzzle.add_between_line([(8, 2), (8, 1), (7, 0), (8, 0)])
    puzzle.add_between_line([(3, 2), (3, 3), (4, 3), (5, 3)])
    puzzle.add_between_line([(7, 8), (8, 8), (7, 7), (8, 7)])
    puzzle.add_between_line([(6, 3), (5, 2), (4, 1), (4, 2)])
    puzzle.add_between_line([(1, 5), (0, 6), (0, 7)])
    puzzle.add_between_line([(6, 7), (6, 6), (5, 7)])
    puzzle.add_between_line([(5, 0), (4, 0), (3, 1)])

    return puzzle
