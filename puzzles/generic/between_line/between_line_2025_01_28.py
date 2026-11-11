"""PuzzleMadness Between Lines Sudoku — 2025-01-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 6, 0, 3, 5, 0, 0, 0, 9],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 4, 0, 0, 0, 3, 8, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 5), (1, 4), (0, 4), (0, 3), (1, 2), (0, 2)])
    puzzle.add_between_line([(0, 8), (0, 7), (1, 8), (2, 8), (1, 7)])
    puzzle.add_between_line([(6, 0), (6, 1), (6, 2), (7, 1), (8, 2)])
    puzzle.add_between_line([(7, 3), (6, 4), (7, 4), (8, 4), (8, 3)])
    puzzle.add_between_line([(4, 0), (3, 1), (2, 1), (3, 0)])
    puzzle.add_between_line([(6, 7), (7, 6), (7, 7), (7, 8)])
    puzzle.add_between_line([(5, 8), (5, 7), (4, 7), (3, 8)])
    puzzle.add_between_line([(6, 3), (5, 3), (4, 2)])
    puzzle.add_between_line([(5, 2), (4, 1), (5, 1)])
    puzzle.add_between_line([(3, 2), (2, 3), (3, 3)])

    return puzzle
