"""PuzzleMadness Between Lines Sudoku — 2025-05-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 1, 0, 7, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [5, 0, 3, 0, 6, 0, 0, 0, 0],
        [6, 5, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 4), (4, 4), (4, 5), (5, 6), (4, 7), (5, 7)])
    puzzle.add_between_line([(2, 5), (1, 4), (0, 3), (0, 4), (1, 5)])
    puzzle.add_between_line([(4, 6), (3, 7), (3, 8), (4, 8), (5, 8)])
    puzzle.add_between_line([(0, 8), (1, 7), (2, 6), (1, 6), (0, 6)])
    puzzle.add_between_line([(6, 4), (7, 4), (6, 3), (6, 2)])
    puzzle.add_between_line([(3, 1), (2, 1), (2, 2), (1, 1)])
    puzzle.add_between_line([(5, 3), (5, 2), (6, 1), (7, 1)])
    puzzle.add_between_line([(6, 5), (7, 6), (8, 7)])
    puzzle.add_between_line([(8, 1), (7, 2), (8, 2)])
    puzzle.add_between_line([(8, 4), (8, 5), (8, 6)])
    puzzle.add_between_line([(6, 6), (7, 7), (6, 7)])

    return puzzle
