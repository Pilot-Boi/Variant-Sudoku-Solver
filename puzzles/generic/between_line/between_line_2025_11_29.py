"""PuzzleMadness Between Lines Sudoku — 2025-11-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 7, 0, 0],
        [0, 0, 0, 4, 2, 5, 8, 0, 0],
        [8, 0, 0, 0, 0, 6, 0, 0, 2],
        [0, 5, 0, 3, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 7), (6, 7), (5, 6), (5, 5), (6, 5), (5, 4)])
    puzzle.add_between_line([(1, 4), (2, 5), (2, 6), (2, 7), (2, 8)])
    puzzle.add_between_line([(7, 5), (6, 4), (7, 4), (8, 5), (8, 4)])
    puzzle.add_between_line([(7, 8), (6, 8), (5, 8), (4, 8), (4, 7)])
    puzzle.add_between_line([(1, 2), (2, 1), (3, 2), (4, 2)])
    puzzle.add_between_line([(4, 0), (5, 1), (6, 2), (6, 1)])
    puzzle.add_between_line([(3, 6), (4, 6), (4, 5), (3, 5)])
    puzzle.add_between_line([(0, 6), (0, 7), (1, 6)])
    puzzle.add_between_line([(0, 1), (1, 1), (1, 0)])
    puzzle.add_between_line([(5, 2), (4, 3), (3, 4)])
    puzzle.add_between_line([(8, 6), (8, 7), (7, 6)])

    return puzzle
