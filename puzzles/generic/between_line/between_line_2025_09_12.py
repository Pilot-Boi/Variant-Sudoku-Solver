"""PuzzleMadness Between Lines Sudoku — 2025-09-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 2, 3, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 8, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 1), (1, 2), (2, 3), (3, 4), (4, 4), (4, 3)])
    puzzle.add_between_line([(8, 2), (8, 3), (7, 2), (6, 2), (6, 1)])
    puzzle.add_between_line([(0, 7), (1, 6), (1, 7), (2, 7), (3, 8)])
    puzzle.add_between_line([(3, 7), (3, 6), (4, 5), (5, 4), (6, 4)])
    puzzle.add_between_line([(1, 3), (1, 4), (2, 4), (2, 5), (2, 6)])
    puzzle.add_between_line([(7, 6), (6, 6), (6, 7), (5, 6)])
    puzzle.add_between_line([(6, 5), (7, 4), (8, 4), (7, 5)])
    puzzle.add_between_line([(3, 1), (3, 2), (4, 1), (5, 1)])
    puzzle.add_between_line([(1, 1), (2, 1), (3, 0)])
    puzzle.add_between_line([(4, 2), (5, 3), (5, 2)])
    puzzle.add_between_line([(7, 8), (6, 8), (5, 8)])

    return puzzle
