"""PuzzleMadness Between Lines Sudoku — 2025-12-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [6, 0, 0, 9, 0, 0, 5, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 4, 0, 0, 5, 0, 7, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 6],
        [0, 7, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 3), (5, 2), (6, 3), (7, 4), (7, 5), (8, 5)])
    puzzle.add_between_line([(2, 4), (2, 5), (3, 4), (4, 3), (5, 4)])
    puzzle.add_between_line([(3, 7), (2, 8), (1, 7), (0, 8), (1, 8)])
    puzzle.add_between_line([(1, 3), (1, 4), (1, 5), (1, 6), (2, 7)])
    puzzle.add_between_line([(7, 3), (8, 2), (8, 1), (7, 1), (7, 0)])
    puzzle.add_between_line([(3, 8), (4, 7), (5, 8), (6, 7)])
    puzzle.add_between_line([(8, 8), (7, 8), (7, 7), (6, 6)])
    puzzle.add_between_line([(3, 0), (4, 0), (5, 0), (5, 1)])
    puzzle.add_between_line([(1, 0), (2, 0), (2, 1), (1, 2)])
    puzzle.add_between_line([(4, 6), (5, 6), (5, 7)])
    puzzle.add_between_line([(4, 5), (3, 5), (3, 6)])
    puzzle.add_between_line([(0, 2), (0, 1), (1, 1)])
    puzzle.add_between_line([(3, 1), (4, 2), (3, 2)])

    return puzzle
