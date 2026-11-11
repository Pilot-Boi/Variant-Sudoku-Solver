"""PuzzleMadness Between Lines Sudoku — 2025-12-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 9, 0, 7],
        [0, 0, 0, 0, 0, 0, 2, 5, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 3), (1, 2), (2, 2), (1, 1), (0, 1), (0, 0)])
    puzzle.add_between_line([(5, 3), (4, 3), (3, 4), (3, 3), (4, 2)])
    puzzle.add_between_line([(6, 4), (5, 4), (6, 5), (7, 5), (8, 6)])
    puzzle.add_between_line([(0, 2), (0, 3), (1, 4), (2, 3), (3, 2)])
    puzzle.add_between_line([(3, 0), (3, 1), (2, 1), (2, 0)])
    puzzle.add_between_line([(6, 2), (7, 2), (7, 1), (8, 1)])
    puzzle.add_between_line([(7, 3), (8, 3), (8, 4), (7, 4)])
    puzzle.add_between_line([(4, 4), (3, 5), (4, 5), (5, 5)])
    puzzle.add_between_line([(0, 4), (0, 5), (0, 6)])
    puzzle.add_between_line([(3, 6), (2, 6), (3, 7)])
    puzzle.add_between_line([(6, 0), (7, 0), (6, 1)])
    puzzle.add_between_line([(5, 2), (4, 1), (5, 1)])

    return puzzle
