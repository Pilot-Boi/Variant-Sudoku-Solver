"""PuzzleMadness Between Lines Sudoku — 2025-12-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 9, 0, 2, 4],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 7, 0, 0, 0, 5, 8, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 5, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 1), (8, 1), (8, 2), (8, 3), (7, 2), (6, 1)])
    puzzle.add_between_line([(6, 0), (5, 0), (4, 0), (5, 1), (6, 2)])
    puzzle.add_between_line([(0, 5), (1, 4), (1, 5), (2, 6), (2, 5)])
    puzzle.add_between_line([(2, 8), (1, 8), (0, 8), (0, 7), (0, 6)])
    puzzle.add_between_line([(7, 6), (6, 7), (7, 7), (6, 8), (5, 8)])
    puzzle.add_between_line([(5, 5), (5, 4), (5, 3), (4, 3)])
    puzzle.add_between_line([(3, 6), (4, 7), (4, 8), (5, 7)])
    puzzle.add_between_line([(6, 3), (7, 3), (7, 4), (7, 5)])
    puzzle.add_between_line([(2, 3), (2, 4), (3, 3)])
    puzzle.add_between_line([(4, 6), (4, 5), (3, 4)])
    puzzle.add_between_line([(0, 1), (0, 2), (0, 3)])

    return puzzle
