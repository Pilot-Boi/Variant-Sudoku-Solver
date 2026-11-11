"""PuzzleMadness Between Lines Sudoku — 2025-01-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 9, 0, 0, 0, 3],
        [4, 0, 0, 0, 0, 0, 5, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 3, 0, 8, 2],
        [0, 0, 0, 0, 2, 0, 0, 0, 5],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 1), (7, 0), (6, 1), (5, 1), (4, 2), (5, 3)])
    puzzle.add_between_line([(3, 3), (4, 3), (3, 2), (2, 1), (2, 2)])
    puzzle.add_between_line([(6, 3), (5, 4), (4, 5), (3, 6), (4, 7)])
    puzzle.add_between_line([(7, 4), (8, 5), (7, 6), (6, 5), (6, 4)])
    puzzle.add_between_line([(3, 7), (2, 6), (1, 6), (2, 7)])
    puzzle.add_between_line([(7, 3), (8, 3), (8, 2), (7, 1)])
    puzzle.add_between_line([(0, 2), (1, 2), (1, 3), (0, 3)])
    puzzle.add_between_line([(6, 6), (5, 7), (4, 8)])
    puzzle.add_between_line([(1, 8), (0, 7), (1, 7)])
    puzzle.add_between_line([(7, 8), (7, 7), (8, 7)])

    return puzzle
