"""PuzzleMadness Between Lines Sudoku — 2025-04-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 4, 0, 1, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 2, 8],
        [7, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 2, 1, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [1, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 7, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 1), (0, 2), (1, 3), (0, 4), (1, 4), (1, 5)])
    puzzle.add_between_line([(5, 1), (4, 0), (3, 0), (3, 1), (4, 1)])
    puzzle.add_between_line([(1, 2), (2, 2), (3, 3), (4, 3), (5, 4)])
    puzzle.add_between_line([(5, 0), (6, 1), (5, 2), (6, 2), (5, 3)])
    puzzle.add_between_line([(7, 8), (6, 7), (5, 6), (6, 6)])
    puzzle.add_between_line([(5, 7), (4, 6), (3, 6), (2, 7)])
    puzzle.add_between_line([(2, 5), (1, 6), (2, 6), (1, 7)])
    puzzle.add_between_line([(6, 3), (7, 3), (8, 3)])
    puzzle.add_between_line([(7, 0), (6, 0), (7, 1)])
    puzzle.add_between_line([(3, 8), (3, 7), (4, 7)])

    return puzzle
