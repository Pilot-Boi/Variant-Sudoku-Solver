"""PuzzleMadness Between Lines Sudoku — 2025-04-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 7, 6, 0, 0, 0, 0],
        [3, 0, 0, 4, 0, 0, 0, 0, 0],
        [9, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 6), (0, 7), (1, 7), (2, 6), (3, 7), (4, 8)])
    puzzle.add_between_line([(3, 1), (3, 0), (4, 0), (5, 1), (5, 0)])
    puzzle.add_between_line([(8, 4), (7, 4), (7, 3), (6, 4), (5, 5)])
    puzzle.add_between_line([(8, 0), (7, 1), (7, 2), (6, 3), (6, 2)])
    puzzle.add_between_line([(4, 4), (3, 3), (3, 4), (2, 4), (2, 5)])
    puzzle.add_between_line([(0, 3), (1, 3), (1, 4), (0, 4)])
    puzzle.add_between_line([(4, 5), (5, 4), (4, 3), (5, 3)])
    puzzle.add_between_line([(3, 6), (4, 7), (5, 7), (6, 8)])
    puzzle.add_between_line([(0, 2), (0, 1), (1, 2), (1, 1)])
    puzzle.add_between_line([(6, 7), (6, 6), (7, 7)])
    puzzle.add_between_line([(7, 0), (6, 0), (6, 1)])
    puzzle.add_between_line([(2, 7), (1, 8), (0, 8)])

    return puzzle
