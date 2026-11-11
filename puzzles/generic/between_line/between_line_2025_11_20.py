"""PuzzleMadness Between Lines Sudoku — 2025-11-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 2, 4, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 5, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 3, 9, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 3), (4, 4), (3, 4), (3, 3), (4, 2), (3, 2)])
    puzzle.add_between_line([(1, 6), (0, 7), (0, 6), (0, 5), (0, 4)])
    puzzle.add_between_line([(6, 8), (5, 8), (4, 7), (3, 6), (4, 6)])
    puzzle.add_between_line([(6, 6), (5, 6), (6, 5), (7, 4), (8, 5)])
    puzzle.add_between_line([(4, 1), (5, 1), (6, 1), (6, 0)])
    puzzle.add_between_line([(5, 0), (4, 0), (3, 0), (3, 1)])
    puzzle.add_between_line([(7, 2), (6, 3), (5, 4), (5, 3)])
    puzzle.add_between_line([(1, 0), (2, 0), (2, 1)])
    puzzle.add_between_line([(5, 5), (4, 5), (3, 5)])
    puzzle.add_between_line([(1, 5), (2, 6), (2, 5)])
    puzzle.add_between_line([(2, 2), (2, 3), (2, 4)])

    return puzzle
