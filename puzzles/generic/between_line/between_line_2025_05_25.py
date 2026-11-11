"""PuzzleMadness Between Lines Sudoku — 2025-05-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 9, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 3, 9, 1],
        [0, 0, 0, 0, 0, 0, 9, 0, 6],
        [0, 5, 0, 0, 0, 3, 0, 0, 0],
        [7, 0, 0, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 5), (8, 4), (8, 3), (8, 2), (7, 2), (8, 1)])
    puzzle.add_between_line([(3, 2), (2, 3), (2, 4), (3, 4), (3, 5)])
    puzzle.add_between_line([(6, 8), (6, 7), (7, 6), (8, 6), (8, 7)])
    puzzle.add_between_line([(8, 0), (7, 1), (6, 2), (5, 1), (6, 0)])
    puzzle.add_between_line([(0, 5), (1, 5), (1, 4), (0, 3), (0, 2)])
    puzzle.add_between_line([(2, 2), (2, 1), (3, 0), (2, 0)])
    puzzle.add_between_line([(5, 0), (4, 0), (3, 1), (4, 1)])
    puzzle.add_between_line([(0, 1), (0, 0), (1, 1), (1, 0)])
    puzzle.add_between_line([(4, 2), (4, 3), (4, 4)])
    puzzle.add_between_line([(5, 3), (6, 3), (7, 3)])
    puzzle.add_between_line([(8, 8), (7, 7), (7, 8)])
    puzzle.add_between_line([(4, 5), (4, 6), (3, 7)])

    return puzzle
