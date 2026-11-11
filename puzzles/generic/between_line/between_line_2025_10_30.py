"""PuzzleMadness Between Lines Sudoku — 2025-10-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 5, 6],
        [0, 0, 0, 0, 9, 6, 0, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 4, 0, 5, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 0), (3, 1), (3, 2), (2, 1), (1, 1), (0, 2)])
    puzzle.add_between_line([(7, 0), (8, 1), (8, 2), (7, 3), (6, 3)])
    puzzle.add_between_line([(5, 4), (5, 5), (4, 6), (3, 7), (3, 6)])
    puzzle.add_between_line([(5, 6), (6, 5), (6, 4), (5, 3), (4, 2)])
    puzzle.add_between_line([(3, 5), (4, 4), (3, 3), (2, 2), (2, 3)])
    puzzle.add_between_line([(7, 7), (6, 6), (6, 7), (6, 8)])
    puzzle.add_between_line([(7, 5), (8, 5), (7, 6), (8, 7)])
    puzzle.add_between_line([(3, 4), (2, 5), (1, 5), (2, 6)])
    puzzle.add_between_line([(2, 8), (2, 7), (3, 8)])
    puzzle.add_between_line([(6, 0), (6, 1), (7, 2)])
    puzzle.add_between_line([(0, 6), (0, 5), (1, 4)])

    return puzzle
