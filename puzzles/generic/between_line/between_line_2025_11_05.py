"""PuzzleMadness Between Lines Sudoku — 2025-11-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 7, 0, 0, 0, 0, 0, 4],
        [0, 8, 4, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 4, 3, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 3, 0, 0, 0, 9],
        [0, 0, 0, 4, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 8), (1, 7), (0, 6), (1, 5), (2, 6), (2, 5)])
    puzzle.add_between_line([(1, 1), (0, 0), (0, 1), (0, 2), (0, 3)])
    puzzle.add_between_line([(4, 1), (4, 0), (3, 1), (2, 2), (1, 2)])
    puzzle.add_between_line([(3, 3), (2, 3), (2, 4), (3, 5), (3, 6)])
    puzzle.add_between_line([(4, 8), (3, 8), (4, 7), (5, 8)])
    puzzle.add_between_line([(8, 5), (7, 5), (7, 6), (8, 6)])
    puzzle.add_between_line([(5, 2), (6, 1), (7, 0), (6, 0)])
    puzzle.add_between_line([(4, 3), (5, 3), (6, 3)])
    puzzle.add_between_line([(7, 4), (8, 4), (7, 3)])
    puzzle.add_between_line([(5, 0), (5, 1), (4, 2)])

    return puzzle
