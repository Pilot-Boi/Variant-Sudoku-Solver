"""PuzzleMadness Between Lines Sudoku — 2025-03-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 7, 0, 0],
        [2, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 7, 0, 9, 0],
        [6, 0, 0, 0, 0, 0, 3, 5, 0],
        [0, 2, 0, 5, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 2],
        [5, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 4), (1, 4), (2, 4), (3, 5), (4, 6), (5, 7)])
    puzzle.add_between_line([(7, 2), (7, 1), (6, 1), (5, 1), (5, 0)])
    puzzle.add_between_line([(6, 4), (7, 4), (8, 5), (8, 4), (7, 3)])
    puzzle.add_between_line([(2, 7), (2, 8), (1, 8), (0, 7), (0, 6)])
    puzzle.add_between_line([(3, 1), (2, 1), (3, 0), (4, 0)])
    puzzle.add_between_line([(3, 2), (3, 3), (4, 3), (5, 4)])
    puzzle.add_between_line([(6, 5), (7, 6), (7, 7), (6, 8)])
    puzzle.add_between_line([(0, 3), (1, 2), (1, 1), (0, 2)])
    puzzle.add_between_line([(3, 7), (4, 7), (3, 6)])
    puzzle.add_between_line([(0, 1), (1, 0), (0, 0)])
    puzzle.add_between_line([(4, 5), (5, 5), (4, 4)])
    puzzle.add_between_line([(2, 6), (1, 7), (1, 6)])

    return puzzle
