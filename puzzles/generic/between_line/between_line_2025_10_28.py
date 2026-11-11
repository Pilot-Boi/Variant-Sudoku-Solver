"""PuzzleMadness Between Lines Sudoku — 2025-10-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 5, 0, 0, 4, 0, 0, 0, 7],
        [8, 4, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 6), (3, 5), (2, 4), (3, 3), (4, 2), (5, 2)])
    puzzle.add_between_line([(2, 7), (1, 7), (2, 8), (3, 7), (4, 7)])
    puzzle.add_between_line([(6, 8), (5, 7), (5, 6), (6, 7), (7, 6)])
    puzzle.add_between_line([(8, 6), (7, 5), (8, 5), (8, 4), (8, 3)])
    puzzle.add_between_line([(0, 4), (1, 3), (1, 4), (2, 5)])
    puzzle.add_between_line([(7, 2), (8, 2), (8, 1), (7, 1)])
    puzzle.add_between_line([(6, 4), (6, 5), (5, 5), (6, 6)])
    puzzle.add_between_line([(3, 0), (2, 0), (1, 0)])
    puzzle.add_between_line([(3, 4), (4, 3), (5, 3)])
    puzzle.add_between_line([(5, 1), (6, 1), (6, 2)])

    return puzzle
