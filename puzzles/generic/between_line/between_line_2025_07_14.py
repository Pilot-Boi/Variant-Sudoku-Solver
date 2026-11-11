"""PuzzleMadness Between Lines Sudoku — 2025-07-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 0, 0, 7, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 8, 2, 5, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 8],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 8, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 4), (0, 5), (1, 6), (2, 6), (2, 5), (1, 5)])
    puzzle.add_between_line([(1, 4), (2, 4), (1, 3), (0, 2), (0, 1)])
    puzzle.add_between_line([(5, 5), (4, 5), (3, 4), (2, 3), (2, 2)])
    puzzle.add_between_line([(6, 4), (7, 5), (8, 6), (7, 7), (7, 6)])
    puzzle.add_between_line([(0, 0), (1, 1), (1, 0), (2, 1), (3, 0)])
    puzzle.add_between_line([(7, 8), (6, 7), (5, 7), (4, 7)])
    puzzle.add_between_line([(0, 6), (1, 7), (1, 8), (2, 7)])
    puzzle.add_between_line([(8, 4), (8, 3), (7, 2), (6, 1)])
    puzzle.add_between_line([(7, 4), (7, 3), (6, 2), (6, 3)])
    puzzle.add_between_line([(6, 5), (5, 6), (6, 6)])
    puzzle.add_between_line([(3, 7), (4, 8), (3, 8)])
    puzzle.add_between_line([(4, 4), (5, 4), (4, 3)])
    puzzle.add_between_line([(6, 0), (7, 1), (8, 2)])

    return puzzle
