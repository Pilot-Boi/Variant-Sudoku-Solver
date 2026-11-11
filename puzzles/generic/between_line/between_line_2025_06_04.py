"""PuzzleMadness Between Lines Sudoku — 2025-06-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 8, 7, 0, 2, 0],
        [0, 0, 2, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 9, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 8), (4, 7), (3, 6), (3, 5), (2, 6), (2, 7)])
    puzzle.add_between_line([(6, 3), (7, 2), (6, 2), (6, 1), (7, 1)])
    puzzle.add_between_line([(4, 6), (5, 6), (5, 5), (4, 5), (3, 4)])
    puzzle.add_between_line([(0, 3), (0, 4), (1, 3), (1, 4), (1, 5)])
    puzzle.add_between_line([(5, 8), (6, 7), (7, 7), (6, 6)])
    puzzle.add_between_line([(7, 6), (7, 5), (8, 4), (7, 3)])
    puzzle.add_between_line([(5, 1), (4, 1), (3, 1), (4, 2)])
    puzzle.add_between_line([(5, 4), (4, 4), (4, 3), (3, 2)])
    puzzle.add_between_line([(1, 6), (2, 5), (2, 4)])
    puzzle.add_between_line([(2, 2), (1, 1), (0, 1)])
    puzzle.add_between_line([(0, 7), (1, 8), (1, 7)])

    return puzzle
