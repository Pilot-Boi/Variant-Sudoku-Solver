"""PuzzleMadness Between Lines Sudoku — 2025-10-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 2, 9, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 3, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 1, 8],
        [0, 0, 0, 8, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 3, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 7), (4, 6), (5, 6), (4, 5), (3, 4), (3, 3)])
    puzzle.add_between_line([(5, 4), (6, 4), (7, 3), (7, 4), (6, 5)])
    puzzle.add_between_line([(4, 0), (4, 1), (3, 1), (4, 2), (5, 1)])
    puzzle.add_between_line([(8, 2), (7, 2), (6, 3), (6, 2), (7, 1)])
    puzzle.add_between_line([(7, 0), (6, 0), (5, 0), (6, 1)])
    puzzle.add_between_line([(3, 6), (3, 5), (2, 4), (1, 5)])
    puzzle.add_between_line([(0, 4), (0, 5), (0, 6), (0, 7)])
    puzzle.add_between_line([(1, 0), (1, 1), (1, 2), (2, 2)])
    puzzle.add_between_line([(1, 8), (2, 8), (1, 7)])
    puzzle.add_between_line([(4, 3), (5, 2), (5, 3)])
    puzzle.add_between_line([(3, 7), (3, 8), (4, 7)])
    puzzle.add_between_line([(1, 3), (0, 3), (1, 4)])

    return puzzle
