"""PuzzleMadness Between Lines Sudoku — 2025-10-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 1, 0, 6, 5, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 5, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 1, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 3],
        [4, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 3, 9, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 3), (0, 4), (1, 4), (2, 4), (3, 5), (3, 6)])
    puzzle.add_between_line([(4, 2), (3, 1), (2, 2), (3, 3), (2, 3)])
    puzzle.add_between_line([(0, 0), (1, 1), (1, 2), (0, 1), (0, 2)])
    puzzle.add_between_line([(0, 5), (0, 6), (1, 7), (2, 8), (1, 8)])
    puzzle.add_between_line([(6, 6), (6, 5), (6, 4), (5, 3), (5, 4)])
    puzzle.add_between_line([(6, 2), (7, 1), (7, 2), (8, 1)])
    puzzle.add_between_line([(4, 8), (5, 7), (4, 6), (5, 6)])
    puzzle.add_between_line([(1, 5), (1, 6), (2, 6), (3, 7)])
    puzzle.add_between_line([(4, 0), (5, 0), (4, 1)])
    puzzle.add_between_line([(6, 3), (7, 3), (8, 3)])
    puzzle.add_between_line([(5, 8), (6, 7), (6, 8)])

    return puzzle
