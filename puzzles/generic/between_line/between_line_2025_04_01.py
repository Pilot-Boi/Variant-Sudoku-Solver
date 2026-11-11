"""PuzzleMadness Between Lines Sudoku — 2025-04-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 1, 7, 8, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 2, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 3, 0, 0, 0, 1, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 5, 0, 0, 9, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 2), (1, 3), (1, 4), (0, 5), (1, 6), (2, 7)])
    puzzle.add_between_line([(2, 5), (3, 4), (4, 5), (5, 4), (6, 3)])
    puzzle.add_between_line([(7, 0), (6, 0), (7, 1), (8, 0), (8, 1)])
    puzzle.add_between_line([(4, 3), (5, 2), (4, 1), (3, 2), (2, 2)])
    puzzle.add_between_line([(3, 8), (3, 7), (4, 8), (5, 7), (6, 8)])
    puzzle.add_between_line([(0, 6), (0, 7), (1, 8), (1, 7)])
    puzzle.add_between_line([(5, 6), (4, 6), (5, 5), (6, 4)])
    puzzle.add_between_line([(7, 8), (7, 7), (6, 7), (7, 6)])
    puzzle.add_between_line([(8, 6), (7, 5), (6, 6), (6, 5)])
    puzzle.add_between_line([(8, 5), (7, 4), (8, 4)])
    puzzle.add_between_line([(6, 1), (7, 2), (6, 2)])
    puzzle.add_between_line([(3, 3), (2, 4), (2, 3)])
    puzzle.add_between_line([(3, 5), (3, 6), (4, 7)])

    return puzzle
