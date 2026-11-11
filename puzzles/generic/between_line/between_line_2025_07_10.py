"""PuzzleMadness Between Lines Sudoku — 2025-07-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [8, 2, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 2, 0, 0, 0, 6],
        [0, 0, 0, 5, 0, 0, 4, 0, 0],
        [0, 0, 3, 4, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 8, 0, 0, 0],
        [0, 6, 0, 0, 0, 5, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 1), (0, 2), (0, 3), (1, 2), (2, 1), (1, 0)])
    puzzle.add_between_line([(3, 1), (2, 0), (3, 0), (4, 0), (5, 0)])
    puzzle.add_between_line([(4, 6), (3, 5), (2, 6), (1, 6), (0, 7)])
    puzzle.add_between_line([(1, 8), (2, 8), (3, 8), (4, 7), (5, 8)])
    puzzle.add_between_line([(7, 6), (6, 6), (7, 7), (7, 8)])
    puzzle.add_between_line([(0, 6), (0, 5), (1, 4), (2, 3)])
    puzzle.add_between_line([(8, 2), (7, 3), (7, 2), (6, 1)])
    puzzle.add_between_line([(8, 7), (8, 6), (7, 5), (6, 5)])
    puzzle.add_between_line([(4, 1), (5, 1), (6, 0)])
    puzzle.add_between_line([(4, 2), (3, 2), (2, 2)])
    puzzle.add_between_line([(6, 3), (6, 2), (5, 2)])
    puzzle.add_between_line([(5, 3), (6, 4), (5, 4)])

    return puzzle
