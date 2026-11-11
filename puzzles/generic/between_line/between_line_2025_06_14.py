"""PuzzleMadness Between Lines Sudoku — 2025-06-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 1, 3],
        [0, 6, 0, 4, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 2, 0, 6, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 4, 6, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 5), (3, 6), (3, 7), (4, 8), (5, 7), (4, 6)])
    puzzle.add_between_line([(5, 4), (6, 4), (7, 4), (8, 4), (8, 3)])
    puzzle.add_between_line([(4, 3), (3, 2), (2, 1), (1, 2), (2, 2)])
    puzzle.add_between_line([(7, 1), (7, 2), (8, 2), (7, 3), (6, 3)])
    puzzle.add_between_line([(4, 2), (5, 3), (6, 2), (5, 1), (5, 2)])
    puzzle.add_between_line([(5, 0), (4, 0), (4, 1), (3, 0)])
    puzzle.add_between_line([(2, 4), (2, 3), (1, 3), (1, 4)])
    puzzle.add_between_line([(5, 6), (6, 5), (7, 6), (6, 7)])
    puzzle.add_between_line([(0, 4), (0, 5), (1, 6), (1, 5)])
    puzzle.add_between_line([(8, 0), (7, 0), (6, 1)])
    puzzle.add_between_line([(4, 5), (4, 4), (3, 4)])
    puzzle.add_between_line([(1, 8), (0, 7), (0, 6)])
    puzzle.add_between_line([(0, 2), (1, 1), (0, 1)])

    return puzzle
