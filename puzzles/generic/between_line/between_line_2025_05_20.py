"""PuzzleMadness Between Lines Sudoku — 2025-05-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 6, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 3, 0, 0, 0, 1, 0, 0],
        [6, 4, 0, 0, 0, 3, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 7), (1, 7), (2, 6), (3, 5), (4, 4), (4, 3)])
    puzzle.add_between_line([(5, 2), (4, 1), (3, 1), (2, 0), (2, 1)])
    puzzle.add_between_line([(1, 6), (0, 6), (1, 5), (0, 4), (1, 4)])
    puzzle.add_between_line([(7, 5), (6, 6), (6, 5), (7, 4), (6, 3)])
    puzzle.add_between_line([(7, 8), (8, 7), (8, 6), (8, 5), (7, 6)])
    puzzle.add_between_line([(6, 4), (5, 3), (5, 4), (4, 5)])
    puzzle.add_between_line([(3, 2), (3, 3), (2, 2), (2, 3)])
    puzzle.add_between_line([(5, 5), (5, 6), (4, 7), (3, 8)])
    puzzle.add_between_line([(0, 0), (0, 1), (0, 2)])
    puzzle.add_between_line([(6, 2), (6, 1), (6, 0)])
    puzzle.add_between_line([(0, 3), (1, 3), (2, 4)])
    puzzle.add_between_line([(8, 4), (8, 3), (8, 2)])

    return puzzle
