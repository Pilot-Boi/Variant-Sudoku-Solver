"""PuzzleMadness Between Lines Sudoku — 2025-01-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 5],
        [0, 6, 8, 5, 0, 0, 0, 2, 0],
        [0, 0, 0, 6, 5, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 4, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 3, 9, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 3), (7, 4), (7, 3), (8, 2), (7, 2), (8, 1)])
    puzzle.add_between_line([(1, 5), (2, 5), (3, 4), (4, 3), (3, 2)])
    puzzle.add_between_line([(1, 1), (0, 0), (1, 0), (2, 1), (2, 2)])
    puzzle.add_between_line([(7, 1), (6, 1), (6, 0), (5, 1), (5, 2)])
    puzzle.add_between_line([(4, 6), (5, 5), (4, 4), (3, 5)])
    puzzle.add_between_line([(7, 5), (6, 5), (6, 4), (6, 3)])
    puzzle.add_between_line([(8, 8), (7, 8), (6, 7), (6, 6)])
    puzzle.add_between_line([(1, 8), (1, 7), (2, 7)])
    puzzle.add_between_line([(0, 5), (1, 6), (0, 6)])
    puzzle.add_between_line([(8, 4), (8, 5), (8, 6)])

    return puzzle
