"""PuzzleMadness Between Lines Sudoku — 2025-12-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 6, 0, 0, 0],
        [0, 9, 1, 0, 0, 0, 8, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 3, 5, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 7, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 4), (0, 4), (1, 3), (2, 4), (3, 3), (2, 3)])
    puzzle.add_between_line([(7, 8), (6, 7), (7, 7), (7, 6), (7, 5)])
    puzzle.add_between_line([(0, 1), (0, 0), (1, 0), (2, 0), (1, 1)])
    puzzle.add_between_line([(1, 6), (2, 7), (2, 8), (1, 8), (0, 7)])
    puzzle.add_between_line([(6, 5), (5, 4), (4, 5), (4, 6), (5, 6)])
    puzzle.add_between_line([(8, 1), (8, 0), (7, 0), (6, 1)])
    puzzle.add_between_line([(8, 5), (7, 4), (8, 3), (8, 4)])
    puzzle.add_between_line([(4, 1), (3, 1), (3, 0), (2, 1)])
    puzzle.add_between_line([(6, 3), (6, 4), (5, 3), (4, 3)])
    puzzle.add_between_line([(3, 2), (2, 2), (1, 2)])
    puzzle.add_between_line([(4, 2), (5, 1), (6, 0)])
    puzzle.add_between_line([(3, 4), (3, 5), (2, 5)])
    puzzle.add_between_line([(8, 2), (7, 1), (7, 2)])

    return puzzle
