"""PuzzleMadness Between Lines Sudoku — 2025-02-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 4, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 4, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 5, 0, 0, 4],
        [0, 0, 0, 6, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 2), (7, 3), (7, 4), (8, 4), (8, 5), (8, 6)])
    puzzle.add_between_line([(2, 5), (3, 6), (3, 5), (4, 4), (4, 3)])
    puzzle.add_between_line([(3, 1), (3, 2), (2, 3), (1, 4), (0, 5)])
    puzzle.add_between_line([(6, 5), (7, 6), (6, 6), (6, 7), (5, 7)])
    puzzle.add_between_line([(5, 1), (6, 1), (7, 1), (6, 2)])
    puzzle.add_between_line([(1, 3), (0, 3), (1, 2), (2, 2)])
    puzzle.add_between_line([(5, 5), (6, 4), (5, 3), (5, 4)])
    puzzle.add_between_line([(4, 0), (3, 0), (2, 0), (2, 1)])
    puzzle.add_between_line([(1, 7), (2, 6), (1, 6)])
    puzzle.add_between_line([(6, 0), (5, 0), (4, 1)])
    puzzle.add_between_line([(8, 0), (8, 1), (7, 0)])
    puzzle.add_between_line([(4, 8), (4, 7), (5, 8)])

    return puzzle
