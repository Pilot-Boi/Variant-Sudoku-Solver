"""PuzzleMadness Between Lines Sudoku — 2025-04-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 8, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 3, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 6, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 4), (5, 4), (6, 3), (6, 2), (7, 1), (8, 2)])
    puzzle.add_between_line([(0, 6), (1, 6), (2, 7), (3, 7), (3, 8)])
    puzzle.add_between_line([(4, 0), (5, 1), (5, 2), (4, 3), (4, 4)])
    puzzle.add_between_line([(5, 5), (6, 5), (5, 6), (4, 6), (4, 5)])
    puzzle.add_between_line([(1, 2), (2, 3), (1, 4), (0, 3)])
    puzzle.add_between_line([(8, 7), (7, 6), (8, 5), (7, 4)])
    puzzle.add_between_line([(2, 0), (2, 1), (1, 1), (0, 1)])
    puzzle.add_between_line([(3, 4), (3, 3), (3, 2), (4, 1)])
    puzzle.add_between_line([(0, 8), (1, 8), (1, 7)])
    puzzle.add_between_line([(0, 5), (0, 4), (1, 5)])
    puzzle.add_between_line([(3, 5), (2, 5), (3, 6)])

    return puzzle
