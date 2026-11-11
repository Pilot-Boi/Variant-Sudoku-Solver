"""PuzzleMadness Between Lines Sudoku — 2025-09-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 8],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 7, 0, 2, 3, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 7, 3, 6, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 8), (7, 8), (8, 7), (7, 6), (7, 7), (6, 7)])
    puzzle.add_between_line([(7, 4), (7, 5), (6, 6), (5, 7), (5, 6)])
    puzzle.add_between_line([(1, 7), (2, 7), (3, 6), (4, 6), (5, 5)])
    puzzle.add_between_line([(4, 0), (4, 1), (5, 0), (5, 1), (5, 2)])
    puzzle.add_between_line([(2, 0), (3, 0), (2, 1), (2, 2)])
    puzzle.add_between_line([(0, 5), (1, 5), (1, 4), (0, 3)])
    puzzle.add_between_line([(7, 2), (6, 3), (5, 4), (4, 5)])
    puzzle.add_between_line([(0, 1), (1, 0), (0, 0)])
    puzzle.add_between_line([(6, 2), (7, 1), (6, 1)])
    puzzle.add_between_line([(3, 7), (2, 8), (1, 8)])

    return puzzle
