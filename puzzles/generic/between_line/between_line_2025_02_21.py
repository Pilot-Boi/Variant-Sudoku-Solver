"""PuzzleMadness Between Lines Sudoku — 2025-02-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 7, 0, 6, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 1, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 9, 7, 0, 0, 0],
        [6, 0, 5, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 2, 0, 0, 0, 0, 3, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 3), (2, 3), (1, 4), (1, 3), (0, 3), (1, 2)])
    puzzle.add_between_line([(5, 1), (4, 0), (5, 0), (6, 1), (6, 0)])
    puzzle.add_between_line([(7, 7), (8, 7), (8, 8), (7, 8), (6, 8)])
    puzzle.add_between_line([(0, 0), (1, 1), (2, 1), (3, 0), (3, 1)])
    puzzle.add_between_line([(2, 7), (2, 6), (1, 6), (2, 5)])
    puzzle.add_between_line([(6, 3), (5, 4), (6, 5), (7, 6)])
    puzzle.add_between_line([(1, 8), (0, 8), (0, 7), (0, 6)])
    puzzle.add_between_line([(4, 2), (3, 2), (2, 2)])
    puzzle.add_between_line([(8, 1), (8, 2), (8, 3)])
    puzzle.add_between_line([(5, 2), (6, 2), (7, 3)])
    puzzle.add_between_line([(7, 1), (8, 0), (7, 0)])

    return puzzle
