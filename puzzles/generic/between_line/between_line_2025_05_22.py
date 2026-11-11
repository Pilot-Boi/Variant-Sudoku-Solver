"""PuzzleMadness Between Lines Sudoku — 2025-05-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 2, 0, 9, 0, 0],
        [0, 0, 0, 1, 9, 3, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 6, 0, 0],
        [0, 0, 0, 5, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [1, 0, 6, 0, 0, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 7), (4, 7), (5, 8), (6, 7), (5, 6), (5, 7)])
    puzzle.add_between_line([(2, 7), (1, 6), (0, 5), (1, 4), (2, 5)])
    puzzle.add_between_line([(3, 1), (2, 1), (3, 0), (4, 0), (4, 1)])
    puzzle.add_between_line([(1, 1), (2, 2), (3, 2), (4, 3), (3, 4)])
    puzzle.add_between_line([(7, 5), (8, 4), (8, 3), (7, 4), (6, 4)])
    puzzle.add_between_line([(0, 2), (1, 2), (0, 1), (0, 0)])
    puzzle.add_between_line([(7, 8), (8, 7), (8, 6), (7, 7)])
    puzzle.add_between_line([(0, 6), (0, 7), (0, 8), (1, 7)])
    puzzle.add_between_line([(1, 3), (2, 3), (2, 4), (3, 3)])
    puzzle.add_between_line([(6, 5), (5, 4), (5, 5)])
    puzzle.add_between_line([(7, 1), (6, 1), (6, 0)])
    puzzle.add_between_line([(4, 2), (5, 3), (4, 4)])
    puzzle.add_between_line([(7, 3), (6, 3), (5, 2)])

    return puzzle
