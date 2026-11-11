"""PuzzleMadness Between Lines Sudoku — 2025-11-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 6, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 2, 0, 1, 0, 0, 0, 0],
        [0, 2, 0, 0, 7, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 7, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 6, 7, 0],
        [4, 0, 0, 7, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 8), (2, 7), (2, 6), (1, 6), (2, 5), (1, 5)])
    puzzle.add_between_line([(2, 0), (2, 1), (3, 2), (2, 2), (1, 2)])
    puzzle.add_between_line([(6, 7), (6, 6), (5, 5), (4, 6), (5, 7)])
    puzzle.add_between_line([(6, 5), (7, 6), (7, 5), (7, 4), (6, 3)])
    puzzle.add_between_line([(4, 7), (3, 6), (4, 5), (4, 4), (3, 3)])
    puzzle.add_between_line([(2, 3), (1, 4), (0, 3), (1, 3)])
    puzzle.add_between_line([(6, 1), (5, 0), (6, 0), (7, 1)])
    puzzle.add_between_line([(0, 7), (1, 8), (1, 7), (0, 6)])
    puzzle.add_between_line([(4, 2), (5, 2), (4, 1)])
    puzzle.add_between_line([(7, 2), (7, 3), (8, 4)])
    puzzle.add_between_line([(1, 1), (0, 1), (1, 0)])
    puzzle.add_between_line([(6, 4), (5, 3), (5, 4)])

    return puzzle
