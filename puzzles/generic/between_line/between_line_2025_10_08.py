"""PuzzleMadness Between Lines Sudoku — 2025-10-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 3, 0, 0],
        [0, 7, 4, 0, 0, 5, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 7, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 3],
        [0, 3, 9, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 7), (1, 7), (2, 8), (2, 7), (3, 7), (4, 7)])
    puzzle.add_between_line([(5, 4), (5, 3), (4, 2), (3, 3), (2, 2)])
    puzzle.add_between_line([(3, 1), (4, 0), (4, 1), (5, 1), (5, 0)])
    puzzle.add_between_line([(1, 6), (2, 6), (1, 5), (2, 4), (2, 5)])
    puzzle.add_between_line([(6, 6), (6, 5), (5, 5), (4, 5)])
    puzzle.add_between_line([(7, 6), (8, 6), (8, 5), (8, 4)])
    puzzle.add_between_line([(8, 7), (8, 8), (7, 8), (7, 7)])
    puzzle.add_between_line([(2, 3), (1, 3), (0, 3), (1, 4)])
    puzzle.add_between_line([(8, 3), (7, 2), (7, 1)])
    puzzle.add_between_line([(5, 6), (4, 6), (5, 7)])
    puzzle.add_between_line([(2, 0), (1, 0), (0, 1)])
    puzzle.add_between_line([(4, 8), (5, 8), (6, 7)])

    return puzzle
