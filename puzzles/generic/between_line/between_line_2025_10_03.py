"""PuzzleMadness Between Lines Sudoku — 2025-10-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 6, 0, 0, 4, 3],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 2],
        [0, 5, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 0), (3, 1), (3, 2), (2, 1), (3, 0), (2, 0)])
    puzzle.add_between_line([(2, 8), (2, 7), (3, 6), (4, 7), (3, 8)])
    puzzle.add_between_line([(1, 3), (2, 2), (2, 3), (1, 4), (1, 5)])
    puzzle.add_between_line([(4, 6), (5, 7), (6, 8), (7, 7), (6, 7)])
    puzzle.add_between_line([(0, 1), (0, 0), (1, 0), (1, 1), (0, 2)])
    puzzle.add_between_line([(5, 6), (4, 5), (5, 5), (6, 4)])
    puzzle.add_between_line([(4, 2), (3, 3), (4, 3), (3, 4)])
    puzzle.add_between_line([(4, 4), (5, 4), (6, 3), (5, 3)])
    puzzle.add_between_line([(6, 1), (6, 2), (7, 3), (8, 3)])
    puzzle.add_between_line([(7, 0), (6, 0), (5, 0)])
    puzzle.add_between_line([(0, 8), (1, 7), (1, 8)])
    puzzle.add_between_line([(0, 4), (0, 3), (1, 2)])
    puzzle.add_between_line([(6, 6), (7, 6), (8, 5)])

    return puzzle
