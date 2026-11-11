"""PuzzleMadness Between Lines Sudoku — 2025-04-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 0, 1, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 6],
        [8, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 6, 0, 9, 0, 0, 2],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 8, 0, 2, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 7), (2, 6), (1, 6), (2, 5), (3, 5), (4, 6)])
    puzzle.add_between_line([(4, 5), (4, 4), (3, 4), (2, 3), (2, 4)])
    puzzle.add_between_line([(6, 5), (7, 6), (8, 5), (7, 4), (6, 3)])
    puzzle.add_between_line([(7, 1), (8, 2), (8, 3), (7, 2), (6, 2)])
    puzzle.add_between_line([(0, 0), (1, 1), (1, 2), (2, 2)])
    puzzle.add_between_line([(3, 1), (4, 1), (5, 0), (5, 1)])
    puzzle.add_between_line([(5, 5), (5, 4), (6, 4), (7, 5)])
    puzzle.add_between_line([(2, 8), (3, 8), (4, 8)])
    puzzle.add_between_line([(2, 0), (2, 1), (3, 0)])
    puzzle.add_between_line([(7, 0), (6, 0), (6, 1)])
    puzzle.add_between_line([(1, 7), (1, 8), (0, 8)])

    return puzzle
