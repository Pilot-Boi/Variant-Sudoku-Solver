"""PuzzleMadness Between Lines Sudoku — 2025-01-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 0, 9, 7, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 7],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 7, 0, 0, 1, 0, 0],
        [0, 0, 0, 8, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 3), (6, 4), (7, 4), (8, 5), (8, 4), (8, 3)])
    puzzle.add_between_line([(4, 6), (3, 7), (2, 8), (1, 8), (0, 7)])
    puzzle.add_between_line([(7, 3), (6, 2), (7, 2), (7, 1), (6, 1)])
    puzzle.add_between_line([(4, 3), (5, 3), (5, 4), (6, 5), (6, 6)])
    puzzle.add_between_line([(7, 8), (8, 7), (7, 7), (7, 6), (8, 6)])
    puzzle.add_between_line([(6, 0), (5, 0), (5, 1), (4, 2)])
    puzzle.add_between_line([(1, 4), (2, 3), (1, 3), (0, 4)])
    puzzle.add_between_line([(1, 5), (2, 5), (2, 4), (3, 5)])
    puzzle.add_between_line([(6, 8), (6, 7), (5, 7), (4, 8)])
    puzzle.add_between_line([(4, 0), (3, 1), (3, 2)])
    puzzle.add_between_line([(2, 2), (1, 1), (1, 2)])
    puzzle.add_between_line([(3, 3), (4, 4), (5, 5)])
    puzzle.add_between_line([(0, 5), (0, 6), (1, 6)])

    return puzzle
