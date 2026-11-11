"""PuzzleMadness Between Lines Sudoku — 2025-01-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 1, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 8, 1, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 4, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 0), (8, 0), (8, 1), (8, 2), (7, 1), (6, 2)])
    puzzle.add_between_line([(3, 7), (2, 7), (2, 6), (1, 5), (0, 4)])
    puzzle.add_between_line([(0, 7), (0, 6), (1, 6), (1, 7), (1, 8)])
    puzzle.add_between_line([(5, 0), (5, 1), (5, 2), (6, 3), (5, 3)])
    puzzle.add_between_line([(3, 6), (4, 5), (3, 4), (3, 3)])
    puzzle.add_between_line([(6, 6), (7, 7), (8, 7), (8, 6)])
    puzzle.add_between_line([(6, 7), (6, 8), (5, 8), (5, 7)])
    puzzle.add_between_line([(2, 2), (1, 1), (2, 1)])
    puzzle.add_between_line([(0, 0), (0, 1), (0, 2)])
    puzzle.add_between_line([(4, 6), (4, 7), (4, 8)])
    puzzle.add_between_line([(2, 4), (2, 3), (1, 3)])

    return puzzle
