"""PuzzleMadness Between Lines Sudoku — 2025-10-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [9, 0, 0, 3, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 2],
        [0, 0, 0, 1, 0, 0, 0, 0, 7],
        [0, 7, 9, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 4, 0, 0, 0, 0],
        [4, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 8, 2, 0, 7, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 5), (4, 4), (3, 4), (2, 3), (1, 4), (0, 4)])
    puzzle.add_between_line([(1, 5), (0, 5), (0, 6), (1, 7), (2, 6)])
    puzzle.add_between_line([(7, 6), (7, 5), (7, 4), (7, 3), (7, 2)])
    puzzle.add_between_line([(8, 7), (8, 8), (7, 7), (6, 7), (7, 8)])
    puzzle.add_between_line([(4, 8), (3, 8), (2, 8), (1, 8)])
    puzzle.add_between_line([(7, 0), (6, 0), (5, 1), (6, 1)])
    puzzle.add_between_line([(1, 0), (0, 0), (1, 1), (2, 2)])
    puzzle.add_between_line([(6, 3), (5, 3), (4, 3)])
    puzzle.add_between_line([(3, 0), (4, 1), (4, 2)])
    puzzle.add_between_line([(4, 5), (4, 6), (4, 7)])

    return puzzle
