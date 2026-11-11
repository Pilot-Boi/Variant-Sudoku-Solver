"""PuzzleMadness Between Lines Sudoku — 2025-02-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 0, 3, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 2, 0, 0, 7, 0, 6, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 9, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 8), (5, 8), (4, 7), (5, 6), (6, 7), (7, 6)])
    puzzle.add_between_line([(2, 6), (3, 5), (3, 6), (4, 6), (4, 5)])
    puzzle.add_between_line([(3, 1), (3, 2), (4, 1), (5, 2), (4, 2)])
    puzzle.add_between_line([(0, 2), (1, 2), (1, 1), (2, 2), (1, 3)])
    puzzle.add_between_line([(0, 8), (1, 7), (1, 8), (2, 7)])
    puzzle.add_between_line([(2, 1), (3, 0), (4, 0), (5, 0)])
    puzzle.add_between_line([(2, 0), (1, 0), (0, 0), (0, 1)])
    puzzle.add_between_line([(5, 3), (4, 4), (5, 5)])
    puzzle.add_between_line([(3, 8), (4, 8), (3, 7)])
    puzzle.add_between_line([(5, 4), (6, 5), (6, 4)])

    return puzzle
