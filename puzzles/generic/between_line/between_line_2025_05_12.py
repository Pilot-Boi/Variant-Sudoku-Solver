"""PuzzleMadness Between Lines Sudoku — 2025-05-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 0, 0, 0, 5],
        [0, 9, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 9],
        [0, 0, 0, 0, 4, 9, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 1, 3, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 1],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 6), (5, 7), (4, 8), (3, 7), (3, 6), (3, 5)])
    puzzle.add_between_line([(4, 4), (4, 3), (3, 2), (4, 1), (4, 2)])
    puzzle.add_between_line([(8, 1), (7, 0), (7, 1), (6, 2), (5, 2)])
    puzzle.add_between_line([(0, 0), (1, 0), (2, 1), (1, 2), (1, 1)])
    puzzle.add_between_line([(0, 1), (0, 2), (1, 3), (1, 4), (0, 4)])
    puzzle.add_between_line([(6, 3), (5, 3), (5, 4), (4, 5)])
    puzzle.add_between_line([(7, 7), (8, 6), (7, 5), (8, 5)])
    puzzle.add_between_line([(2, 0), (3, 1), (2, 2), (2, 3)])
    puzzle.add_between_line([(5, 1), (4, 0), (3, 0)])
    puzzle.add_between_line([(1, 8), (0, 7), (0, 8)])
    puzzle.add_between_line([(3, 3), (3, 4), (2, 4)])
    puzzle.add_between_line([(3, 8), (2, 8), (2, 7)])

    return puzzle
