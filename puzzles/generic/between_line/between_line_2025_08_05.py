"""PuzzleMadness Between Lines Sudoku — 2025-08-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [5, 0, 2, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 2],
        [0, 0, 0, 0, 0, 4, 9, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 8), (1, 7), (2, 7), (1, 6), (2, 5), (2, 4)])
    puzzle.add_between_line([(8, 2), (8, 1), (7, 1), (7, 2), (6, 2)])
    puzzle.add_between_line([(5, 4), (4, 5), (5, 5), (6, 4), (6, 5)])
    puzzle.add_between_line([(3, 7), (3, 6), (4, 7), (5, 8), (5, 7)])
    puzzle.add_between_line([(4, 2), (5, 1), (6, 0), (5, 0), (4, 1)])
    puzzle.add_between_line([(8, 4), (8, 5), (7, 5), (7, 4)])
    puzzle.add_between_line([(4, 0), (3, 1), (2, 0), (3, 0)])
    puzzle.add_between_line([(7, 0), (6, 1), (5, 2), (4, 3)])
    puzzle.add_between_line([(0, 2), (1, 1), (1, 2), (1, 3)])
    puzzle.add_between_line([(4, 4), (3, 4), (3, 3)])
    puzzle.add_between_line([(2, 3), (3, 2), (2, 2)])
    puzzle.add_between_line([(6, 6), (6, 7), (6, 8)])
    puzzle.add_between_line([(6, 3), (7, 3), (8, 3)])

    return puzzle
